
import os

def get_bothMid(filepath):
    leftGot = []
    rightGot = []
    for line in open(filepath):
        line = line.strip()
        if "Front Left" in line:
            midstr = line.split(",")[-1]
            ifGet = midstr.split(":")[-1]
            leftGot.append(ifGet)
        if "Front Right" in line:
            midstr = line.split(",")[-1]
            ifGet = midstr.split(":")[-1]
            rightGot.append(ifGet)

    print(leftGot, rightGot)
    if len(leftGot) != len(rightGot):
        print("ERROR, not match")
        return -1, -1

    bothCnt = 0
    diffCnt = 0
    for i, got in enumerate(leftGot):
        if got == '1' and rightGot[i] == '1':
            bothCnt += 1
        else:
            diffCnt += 1
    print(bothCnt, diffCnt)
    return bothCnt, diffCnt



def get_sapMidStatisticWholeFile(filepath):
    leftGot = []
    rightGot = []
    beginInsert = False
    for line in open(filepath):
        if "[DockInsert_StateID_ApproachDock] start" in line:
            print(line.strip())
            beginInsert = True
            continue

        if not beginInsert: continue

        line = line.strip()
        if "Front Left -> bOnyxL2S:" in line:
            midstr = line.split("Mid:")[-1]
            ifGet = midstr.strip()
            leftGot.append(ifGet)
            continue
            #print(line)

        if "Front Right -> bOnyxL2S:" in line:
            midstr = line.split("Mid:")[-1]
            ifGet = midstr.strip()
            rightGot.append(ifGet)
            continue
            #print(line)

        if "[D] Dock Connected" in line:
            #statistic
            bothCnt = 0
            diffCnt = 0
            beginStat = False
            for i, got in enumerate(leftGot):
                if got == '1' and rightGot[i] == '1':
                    bothCnt += 1
                    beginStat = True
                elif beginStat:
                    diffCnt += 1

            print(len(leftGot), len(rightGot))
            print(line, bothCnt, diffCnt, "\n")
            beginInsert = False
            leftGot = []
            rightGot = []

    if len(leftGot) != len(rightGot):
        print("ERROR, not match")
        return -1, -1


def get_tanossliteMid(filepath):
    leftGot = []
    rightGot = []
    beginInsert = False
    startCount = False
    for line in open(filepath):
        if "CHARGER STATE: RCS_InsertCharger" in line:
            beginInsert = True
            continue

        if not beginInsert: continue

        if "CGI Approach [1:" in line and beginInsert and not startCount:
            print(line)
            leftGot = []
            rightGot = []
            startCount = True
            continue

        if not startCount: continue

        line = line.strip()
        if "[PL6] 1 [FL]" in line:
            midstr = line.split("Mid")[-1]
            ifGet = midstr.strip()
            leftGot.append(ifGet)
            #print(line)

        if "[PL6] 1 [FR]" in line:
            midstr = line.split("Mid")[-1]
            ifGet = midstr.strip()
            rightGot.append(ifGet)
            #print(line)

        if "Moving forward is over" in line and startCount:
            print(line)
            print(len(leftGot),len(rightGot))
            #statistic
            bothCnt = 0
            diffCnt = 0
            for i, got in enumerate(leftGot):
                if got == '1' and rightGot[i] == '1':
                    bothCnt += 1
                else:
                    diffCnt += 1

            print(os.path.dirname(filepath) ,bothCnt, diffCnt, "\n\n")
            return bothCnt, diffCnt

    if len(leftGot) != len(rightGot):
        print("ERROR, not match")
        return -1, -1


#1.找到压缩文件，解压到同级目录
#2.查找到所有Nav_normal.log文件
#3.解析异常的文件内容，包括：正常充电，充电掉桩，二次上桩(细分clifff)，失败等等，导出结果
    #正常模式：
    #非正常模式：
        #充电掉桩：有重连状态
        #二次上桩：是否有movaback
        #失败报错

import collections

dupInsertAction = ['MoveBackFromDock', 'No power']
successInsertAction = ['RCS_InsertCharger', 'RCS_Charging', 'ConnectingDock State finished']

def find_files(file_dir, navpattern, eventpattern):
    navFiles = []
    eventFiles = []

    for root, dirs, files in os.walk(file_dir):
        for file in files:
            curbasename = os.path.basename(root)
            curDirname = os.path.dirname(root)
            if navpattern in file:
                navFiles.append(curDirname + "/" + curbasename + '/' + file)
            if eventpattern in file:
                eventFiles.append(curDirname + "/" + curbasename + '/' + file)
    return navFiles, eventFiles

def parse_event_file(eventfile, reports):
    f = open(eventfile, 'r')

    curDirname = os.path.dirname(eventfile)
    for line in f.readlines():
        if "ErrorCode = 4" in line:
            reports['errorCode=4'].append(curDirname)
            break

        if "ErrorCode = 7" in line:
            reports['errorCode=7'].append(curDirname)
            break

def removeDupRecord(srcDirname, reports):
    for action in dupInsertAction:
        if srcDirname in reports[action]:
            reports[action].remove(srcDirname)
            print("remove dup dirname: %s", srcDirname)

def parse_nav_file(navfile, reports):
    f = open(navfile, 'r')

    curDirname = os.path.dirname(navfile)
    hasException = False
    contents = []
    for line in f.readlines():
        if hasException == False and 'StateReconnectToDock::' in line:
            hasException = True
            reports['StateReconnectToDock'].append(curDirname)
            break

        if 'ReturnChargerIR::BackToStartPoint' in line:
            hasException = True
            reports['ReturnChargerIR::BackToStartPoint'].append(curDirname)
            removeDupRecord(curDirname, reports)
            break

        for action in dupInsertAction:
            if hasException == False and action in line:
                hasException = True
                reports[action].append(curDirname)

        for normalAction in successInsertAction:
            if normalAction in line:
                contents.append(line)

    if hasException == False and len(contents) == 3:
        reports['SUCCESS'].append(curDirname)

def parse_navnormal_dir(file_dir, reportFilePath):
    navFiles, eventFiles = find_files(file_dir, "NAV_normal_m.log", "EVENTTASK_normal.log")

    reports = collections.defaultdict(list)
    for navfile in navFiles:
        parse_nav_file(navfile, reports)

    for eventfile in eventFiles:
        parse_event_file(eventfile, reports)
    print(reports)

    reportFile = open(reportFilePath, 'w+')
    for state, files in reports.items():
        stateCnt = len(files)
        curline = "%s : %d\n" % (state, stateCnt)
        reportFile.write(curline)

    for state, files in reports.items():
        if state == 'SUCCESS': continue
        reportFile.write('\n\n' + state+': \n')
        for file in files:
            reportFile.write(file + '\n')

    reportFile.close()


def parse_laser_file(laserfile):
    f = open(laserfile, 'r')

    curDirname = os.path.dirname(laserfile)
    newLaserFile = os.path.join(curDirname, "newLaser.txt")
    contents = []
    for line in f.readlines():
        contents = line.split(' ')
        break

    wf = open(newLaserFile, "w+")
    angle = 0
    range = 0
    for i, item in enumerate(contents):
        item = item.strip()
        if len(item) == 0: break

        # 0 1 2 3 4 5 6 7 8
        if (i+1)%3 == 1:
            angle = float(item)*180/3.14
        elif (i+1)%3 == 2:
            range = float(item)*100
        elif (i+1)% 3 == 0:
            isFilter = int(item) & int(0x2000)
            intensity = int(item) & int(0x0FFF)
            isValid = ((int(item) & int(0x8000)) == 0)
            isOk = ((int(item) & int(0x0FFF)) > 200)
            isOK2 = ((int(item) & int(0x4000)) == 0)
            curline = "angle: %f, range: %d, intensity: %d, isFilter: %d, isOk: %d, isValid: %d, isOK2: %d\n" % (angle, range, int(intensity), bool(isFilter), bool(isOk), bool(isValid), bool(isOK2))
            #print(curline)
            print(item, isFilter, intensity)
            wf.write(curline)

    wf.close()


laserFilePath = "D:/data/log/laser.txt"
parse_laser_file(laserFilePath)

'''
srcDir = "D:/data/log/temp/retest/"
reportFilePath = "D:/data/log/temp/stat_retest.log"
parse_navnormal_dir(srcDir, reportFilePath)
'''

#filepath = "D:/data/log/temp/insertlog/sap/上限/rrlog.log.581"
#get_sapMidStatisticWholeFile(filepath)
#get_tanossliteMid(filepath)
#print("filepath: %s, both have mid : %d,  not both: %d", filepath, bc, df)
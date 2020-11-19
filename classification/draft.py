#coding=utf-8

from sklearn import datasets
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

np.random.seed(1)

class K_Means(object):
    # k是分组数；tolerance‘中心点误差’；max_iter是迭代次数
    def __init__(self, ):
        self.sp_kmeans = None

    def myKNN(self, S, k, sigma=1.0):
        N = len(S)
        A = np.zeros((N, N))

        for i in range(N):
            dist_with_index = zip(S[i], range(N))
            dist_with_index = sorted(dist_with_index, key=lambda x: x[0])
            neighbours_id = [dist_with_index[m][1] for m in range(k + 1)]  # xi's k nearest neighbours

            for j in neighbours_id:  # xj is xi's neighbour
                A[i][j] = np.exp(-S[i][j] / 2 / sigma / sigma)
                A[j][i] = A[i][j]  # mutually

        return A

    def calLaplacianMatrix(self, adjacentMatrix):
        # compute the Degree Matrix: D=sum(A)
        degreeMatrix = np.sum(adjacentMatrix, axis=1)

        # compute the Laplacian Matrix: L=D-A
        laplacianMatrix = np.diag(degreeMatrix) - adjacentMatrix

        # normailze
        # D^(-1/2) L D^(-1/2)
        sqrtDegreeMatrix = np.diag(1.0 / (degreeMatrix ** (0.5)))
        return np.dot(np.dot(sqrtDegreeMatrix, laplacianMatrix), sqrtDegreeMatrix)

    def euclidDistance(self, x1, x2, sqrt_flag=False):
        res = np.sum((x1 - x2) ** 2)
        if sqrt_flag:
            res = np.sqrt(res)
        return res

    def calEuclidDistanceMatrix(self, X):
        X = np.array(X)
        S = np.zeros((len(X), len(X)))
        for i in range(len(X)):
            for j in range(i + 1, len(X)):
                S[i][j] = 1.0 * self.euclidDistance(X[i], X[j])
                S[j][i] = S[i][j]
        return S

    def fit(self, data):
        Similarity = self.calEuclidDistanceMatrix(data)
        Adjacent = self.myKNN(Similarity, k=10)
        Laplacian = self.calLaplacianMatrix(Adjacent)

        x, V = np.linalg.eig(Laplacian)
        x = zip(x, range(len(x)))
        x = sorted(x, key=lambda x: x[0])

        H = np.vstack([V[:, i] for (v, i) in x[:500]]).T
        self.sp_kmeans = KMeans(n_clusters=2).fit(H)

    def predict(self, p_datas):
        result = self.sp_kmeans.predict(p_datas)

        return result

def genTwoCircles(n_samples=1000):
    X,y = datasets.make_circles(n_samples, factor=0.5, noise=0.05)
    return X, y

if __name__ == '__main__':

    data, label = genTwoCircles(n_samples=500)
    k_means = KMeans(n_clusters=2)
    k_means.fit(data)

    cat = k_means.predict(data)
    plt.scatter(data[0], data[1], c=cat, marker='x')
    plt.show()

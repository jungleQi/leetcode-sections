class Map
{
    public:
        vector<Node*> NodeSet;
        vector<Point> walls;
        Point size_;
        int directions;

        void Set_diag_move(bool enable) { directions = (enable ? 8 : 4); };

        void Set_size(Point size) { size_ = size; };
        void addCollision(Point coordinates);
        void removeCollision(Point coordinates);
        void clearCollisions();

        void releaseNodes(vector<Node*> nodes);
        Node* findNodeOnList(vector<Node*> nodes_, Point coordinates_);
        Point getDelta(Point source, Point target);

        int manhattan(Point source, Point target);

        bool Detect_collision(Point coordinates);

        vector<A_star::Point> findPath(Point source, Point target);
};
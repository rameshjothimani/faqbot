class BinaryTree(object):
    def __init__(self):
        self.left = None;
        self.right = None;
        self.data = None;


root = BinaryTree();
root.data = "root";
root.left = BinaryTree();
root.left.data = "left";
root.right = BinaryTree();
root.right.data = "right";

print(root.left.data);

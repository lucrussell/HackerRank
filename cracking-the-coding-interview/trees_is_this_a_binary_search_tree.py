""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
INT_MAX = 4294967296
INT_MIN = -4294967296

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBSTUtil(node, mini, maxi):
    if node is None:
        return True

    if node.data < mini or node.data > maxi:
        return False

    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


def checkBST(root):
    return (isBSTUtil(root, INT_MIN, INT_MAX))

if __name__ == '__main__':
    checkBST()
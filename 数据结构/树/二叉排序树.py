# 二叉排序树：
# 若左子树非空，左子树所有节点值小于根节点值
# 若右子树非空，右子树所有节点值大于根节点值
# 左右子树也是二叉排序树

#  二叉排序树的建立：递归插入
class BiTree:
    # 二叉树的定义
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def InsertBST(num, root):
    if root is None:
        root = BiTree(num)
    elif num < root.val:
        root.left = InsertBST(num, root.left)
    else:
        root.right = InsertBST(num, root.right)
    return root

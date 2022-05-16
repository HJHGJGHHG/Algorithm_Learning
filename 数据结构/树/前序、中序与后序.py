class BiTree:
    # 二叉树的定义
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的遍历：前、中、后（根据根节点在根节点、左子树、右子树的访问顺序决定）
# 1. 给定遍历序列，构造二叉树
# e.g. http://t.cn/AiKuUTlX
def createBiTree(string):
    c = string.pop()
    if c == "#":
        return None
    # 由前序建树
    root = BiTree(c)
    root.left = createBiTree(string)
    root.right = createBiTree(string)
    return root


# 2.给定二叉树，得到遍历序列
def InOrder(root):
    # 中序遍历
    if root is None:
        return
    InOrder(root.left)
    print(root.val)
    InOrder(root.right)
    return


# 3. 由前序、中序确定后序
# 先确定根节点，而后将两个序列按根节点切分，然后递归
def PreandIn2Post(preorder, inorder):
    if len(preorder) == 0:
        return None
    c = preorder[0]
    root = BiTree(c)
    pos = inorder.index(c)
    root.left = PreandIn2Post(preorder[1:pos + 1], inorder[0:pos + 1])
    root.right = PreandIn2Post(preorder[pos + 1:], inorder[pos + 1:])
    return root



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = []
    
    def inorderTraversal(self, root):
        """
        中序遍历二叉树：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

        :type root: TreeNode
        :rtype: List[int]
        """
        #递归
        #时间复杂度O(n)
        # if root:
        #     self.inorderTraversal(root.left)
        #     self.result.append(root.val)
        #     self.inorderTraversal(root.right)
        # return self.result
        
        #迭代
        #时间复杂度O(n)
        stack = []
        e = root
        while stack or e:
            while e:
                stack.append(e)
                e = e.left
            ele = stack.pop()
            self.result.append(ele.val)
            e = ele.right
        return self.result
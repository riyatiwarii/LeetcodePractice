'''Binary Tree Paths'''
def rootToLeafPaths(self, root):
   if not root: return []
   if not root.left and not root.right: return [str(root.val)]
   return [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.left)] +
             [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.right)]
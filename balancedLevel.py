class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)


def sameLevel(root) -> bool:
    level = 0
    queue = [root]
    values={}
    leaf=[]
    while len(queue):
        sizeOflevel=len(queue)
        while sizeOflevel:
            current=queue.pop(0)
            if level not in values:
                values[level]=[]
            values[level].append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if not current.right and not current.left:
                leaf.append(current.value)
            sizeOflevel-=1
        level+=1
    return leaf==values[level-1]

# def sameLevel(root):
#     leaves=set()
#     sameLevelHelper(root,leaves)
#     return len(leaves)==1

# def sameLevelHelper(root,leaves,level=0):
#     if root is None:
#         return
#     if  root.right is None and root.left is None:
#         leaves.add(level)
#     if root.left is not  None:
#         sameLevelHelper(root.left,leaves,level+1)
#     if  root.right is not  None:
#         sameLevelHelper(root.right,leaves,level+1)

t = BinaryTree(3)   
t.insert(1)
t.insert(4)
t.insert(0)
t.insert(5)
t.insert(6)
t.insert(-1)
print(sameLevel(t))

#    3
#  1   4 
# 0      5
#          6
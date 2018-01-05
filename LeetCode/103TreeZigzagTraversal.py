from collections import deque
import pdb

class TreeNode(object):
    def __init__(self):
        self.val = None 
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    pdb.set_trace()
    q = deque([root])
    result = []

    left2right = True
    while any(item for item in q):
        nodeVals = [item.val for item in q if item]
        result.append(nodeVals)
        temp = deque([])

        while q:
            node = q.popleft() if left2right else q.pop()
            if node:
                if not left2right:
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    temp.append(node.right)
                    temp.append(node.left)
        q = temp
        left2right = not left2right
    return result

def main():
    g = TreeNode()
    g.val = 7
    g.left = None
    g.right = None

    f = TreeNode()
    f.val = 15
    f.left = None
    f.right = None

    c = TreeNode()
    c.val = 20
    c.left = f
    c.right = g

    b = TreeNode()
    b.val = 9
    b.left = None
    b.right = None

    a = TreeNode()
    a.val = 3
    a.left = b
    a.right = c

    print(zigzagLevelOrder(a))

if __name__ == '__main__':
    main()

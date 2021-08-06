class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        indentation = self.getLevel()
        print("   " * indentation + "|__" + self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    macbookPro = TreeNode("Macbook Pro")
    tv = TreeNode("Television")
    cellphone = TreeNode("Cellphone")
    
    root.add_child(laptop)
    laptop.add_child(macbookPro)
    laptop.add_child(TreeNode('Alienware'))
    laptop.add_child(TreeNode('Thinkpad'))

    root.add_child(tv)
    tv.add_child((TreeNode('Hisense')))
    tv.add_child((TreeNode('Samsung')))
    tv.add_child((TreeNode('LG')))

    root.add_child(cellphone)
    cellphone.add_child(TreeNode('iOS'))
    cellphone.add_child(TreeNode('android'))
    
    root.add_child(TreeNode('Toys'))
    
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.printTree()
    pass
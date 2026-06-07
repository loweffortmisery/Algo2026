class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def pre_order(self):
        res = self.key
        if self.left is not None:
            res += self.left.pre_order()
        if self.right is not None:
            res += self.right.pre_order()
        return res


if __name__ == "__main__":
    with open("input.txt") as f:
        words = f.read().split()
        
    chars = []
    
    for word in words:
        if word == '*':
            break
        chars.extend(list(word))
        
    if chars:
        chars.reverse()
        tree = BinaryTree(chars[0])
        for i in range(1, len(chars)):
            tree.insert(chars[i])
        print(tree.pre_order())

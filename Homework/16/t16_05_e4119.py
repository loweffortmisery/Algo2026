class Tree:
    def __init__(self, key, parent=None):
        self.parent = parent
        self.key = key  
        self.children = []

    def __str__(self):
        return str(self.key)

    def dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node

    def add(self, parent_key, key):
        parent = self.dfs(parent_key)
        node = Tree(key, parent)
        parent.children.append(node)

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child
        return None

    def print_tree(self, depth=-1):
        self.children.sort(key=lambda node: node.key)
        
        if depth >= 0:
            print(" " * depth + self.key)
            
        for child in self.children:
            child.print_tree(depth + 1)


if __name__ == "__main__":
    with open("input.txt") as f:
        N = int(f.readline().strip())
        
        tree = Tree("ROOT")
        
        for _ in range(N):
            path = f.readline().strip()
            if not path:
                continue
                
            parts = path.split('\\')
            current_node = tree
            
            for part in parts:
                child = current_node.get_child(part)
                
                if not child:
                    child = Tree(part, current_node)
                    current_node.children.append(child)
                    
                current_node = child
                
        tree.print_tree()

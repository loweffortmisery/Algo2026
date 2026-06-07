class Tree:
    def __init__(self, key, parent=None):
        self.parent = parent
        self.key = key
        self.children = []
        self.fee = 0  # Додано атрибут для збереження офіційного збору

    def __str__(self):
        return str(self.key)

    def dfs(self, key):
        if self.key == key:
            return self
        for child in self.children:
            node = child.dfs(key)
            if node is not None:
                return node

    def add(self, parent_key, key, fee):
        parent = self.dfs(parent_key)
        node = Tree(key, parent)
        node.fee = fee
        parent.children.append(node)

    def get(self, a, b):
        node = self.dfs(a)
        came_from = None

        while node is not None:
            if node.key == b:
                return node.key
            for child in node.children:
                if child is not came_from and child.dfs(b) is not None:
                    return node
            came_from = node
            node = node.parent

    def execute(self, command):
        method, *args = command.split()
        method = method.lower()
        args = map(int, args)
        return getattr(self, method)(*args)

    def find_min_fee(self):
        if not self.children:
            return self.fee
        return self.fee + min(child.find_min_fee() for child in self.children)


if __name__ == "__main__":
    with open("input.txt") as f:
        N = int(f.readline())
        
        employees = [0] * (N+1)
        for i in range(1, N + 1):
            employees[i] = list(map(int, f.readline().split()))
            
        tree = Tree(1)
        tree.fee = employees[1][0]
        
        queue = [1]
        
        while queue:
            current_id = queue.pop()
            children = employees[current_id][2:]
            
            for child_id in children:
                child_fee = employees[child_id][0]
                child_node = tree.add(current_id, child_id, child_fee)
                queue.append(child_id)
                
        print(tree.find_min_fee())

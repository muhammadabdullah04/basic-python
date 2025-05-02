class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # Visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.add_child(element)
    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build_tree(numbers)

    print("In-order traversal:", tree.in_order_traversal())
    print("Pre-order traversal:", tree.pre_order_traversal())
    print("Post-order traversal:", tree.post_order_traversal())
    print("Minimum value:", tree.find_min())
    print("Maximum value:", tree.find_max())
    print("Sum of all values:", tree.calculate_sum())

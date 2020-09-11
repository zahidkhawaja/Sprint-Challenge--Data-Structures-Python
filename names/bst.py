# Using our binary search tree to optimize our names.py solution
# We specifically need the 'insert' and 'contains' methods for our use case

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # Left case
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Recursive call of insert method
                self.left.insert(value)
        # Right case
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True
        # Left case
        if target < self.value:
            if self.left is None:
                return False
            else:
                # Recursive call of contains method
                return self.left.contains(target)
        # Right case
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
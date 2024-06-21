"""A class represnting a node in an AVL tree"""
class AVLNode(object):
    """Constructor, you are allowed to add more fields.
    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor = None
        self.height = -1
        self.size = 0

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """
    def get_key(self):           # O(1)
        return self.key if self.is_real_node() else None

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """
    def get_value(self):           # O(1)
        return self.value if self.is_real_node() else None

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """
    def get_left(self):           # O(1)
        return self.left if self.is_real_node() else None

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """
    def get_right(self):           # O(1)
        return self.right if self.is_real_node() else None

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """
    def get_parent(self):           # O(1)
        return self.parent if self.parent.is_real_node() else None

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """
    def get_height(self):           # O(1)
        return self.height if self.is_real_node() else -1

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """
    def get_size(self):           # O(1)
        return self.size if self.is_real_node() else 0

    """sets key

    @type key: int or None
    @param key: key
    """
    def set_key(self, key):           # O(1)
        self.key = key
        return

    """sets value

    @type value: any
    @param value: data
    """
    def set_value(self, value):       # O(1)
        self.value = value
        return

    """sets left child

    @type node: AVLNode
    @param node: a node
    """
    def set_left(self, node):         # O(1)
        self.left = node
        return

    """sets right child

    @type node: AVLNode
    @param node: a node
    """
    def set_right(self, node):           # O(1)
        self.right = node
        return

    """sets parent

    @type node: AVLNode
    @param node: a node
    """
    def set_parent(self, node):           # O(1)
        self.parent = node
        return

    """sets the height of the node

    @type h: int
    @param h: the height
    """
    def set_height(self, h):           # O(1)
        self.height = h
        return

    """sets the size of node

    @type s: int
    @param s: the size
    """
    def set_size(self, s):           # O(1)
        self.size = s
        return

    """sets the balance factor of a node"""

    def set_bf(self):           # O(1)
        left_height = self.left.height if self.is_real_node() else 0
        right_height = self.right.height if self.is_real_node() else 0
        self.balance_factor = left_height - right_height
        return

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def is_real_node(self):           # O(1)
        if self.key is not None:
            return True
        else:
            return False

    def create_virtuals(self):           # O(1)
        if self.right is None:
            self.right = AVLNode(None, None)
            self.right.parent = self

        if self.left is None:
            self.left = AVLNode(None, None)
            self.left.parent = self
        return


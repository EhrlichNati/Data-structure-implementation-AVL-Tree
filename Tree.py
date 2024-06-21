
"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """
    def __init__(self):
        self.root = AVLNode(None, None)
        self.root.parent = AVLNode(None, None)

    """searches for a node in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key.
    """
    def search(self, key):              # O(log(n))
        # search node with key if key is in the tree, else  return None
        node = self.root
        while node.is_real_node():
            if node.key == key:
                return node
            elif key > node.key:
                node = node.right
            else:
                node = node.left
        return None


    """rotate subtrees of balance factor criminal """

    def rotate(self, criminal, rotate_side='right'):           # O(1)
        son_side = 'left'
        if rotate_side != 'right':
            son_side = 'right'

        son = getattr(criminal, son_side)
        son_child = getattr(son, rotate_side)

        setattr(criminal, son_side, son_child)
        son_child.parent = criminal
        setattr(son, rotate_side, criminal)
        son.parent = criminal.parent

        if criminal.parent.is_real_node():
            if criminal.parent.key > son.key:
                son_side = 'left'
            else:
                son_side = 'right'
            setattr(son.parent, son_side, son)
            criminal.parent = son
        else:
            setattr(son, rotate_side, criminal)
            criminal.parent = son
            self.root = son

        return

    """check if tree is unbalanced after insert new node"""

    def fixing_after_insertion(self, new_node):              # O(log(n))
        # calculate height and balance factor
        curr_node = new_node.parent
        cnt_rebalanced = 0
        did_rotation = False
        fixing_pointer = new_node
        while curr_node.is_real_node():
            prev_height = curr_node.height
            self.calc_height(curr_node)

            # find bf criminal and rotate the subtree if necessary
            if -2 < curr_node.balance_factor < 2:
                if prev_height == curr_node.height:
                    break
                else:
                    cnt_rebalanced += 1
                    curr_node = curr_node.parent
                    continue
            elif curr_node.balance_factor == 2:
                did_rotation = True
                if curr_node.left.balance_factor == 1:
                    fixing_pointer = curr_node.left
                    self.rotate(curr_node, 'right')
                    cnt_rebalanced += 1
                    break
                else:
                    fixing_pointer = curr_node.left.right
                    self.rotate(curr_node.left, 'left')
                    self.rotate(curr_node, 'right')
                    cnt_rebalanced += 2
                    break
            else:
                # curr_node.balance_factor == -2
                did_rotation = True
                if curr_node.right.balance_factor == -1:
                    fixing_pointer = curr_node.right
                    self.rotate(curr_node, 'left')
                    cnt_rebalanced += 1
                    break
                else:
                    fixing_pointer = curr_node.right.left
                    self.rotate(curr_node.right, 'right')
                    self.rotate(curr_node, 'left')
                    cnt_rebalanced += 2
                    break

        return cnt_rebalanced, did_rotation, fixing_pointer


    """calculate node's height and set the new value + balance factor"""

    def calc_height(self, node):              # O(1)
        if node.is_real_node():
            left_height = node.left.height
            right_height = node.right.height
            height = max(left_height, right_height) + 1
            node.set_height(height)
            node.set_bf()

        return


    """calculate node's size and set the new value"""

    def calc_size(self, node):              # O(1)
        if node.is_real_node():
            left_size = node.left.size
            right_size = node.right.size
            size = left_size + right_size + 1
            node.set_size(size)
        return


    """update heights and balance factor after insert or delete new node"""

    def update(self, did_rotation, fixing_pointer):              # O(log(n))
        if fixing_pointer.is_real_node():
            if did_rotation is False:
                # update after no rotate
                while fixing_pointer.is_real_node():
                    self.calc_height(fixing_pointer)
                    self.calc_size(fixing_pointer)
                    fixing_pointer = fixing_pointer.parent
            else:
                # update after rotation
                self.calc_height(fixing_pointer.left)
                self.calc_size(fixing_pointer.left)
                self.calc_height(fixing_pointer.right)
                self.calc_size(fixing_pointer.right)
                self.calc_height(fixing_pointer)
                self.calc_size(fixing_pointer)
        return


    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def insert(self, key, val):              # O(log(n))
        new_node = AVLNode(key, val)
        curr_node = self.root
        parent_node = self.root.parent

        while curr_node.is_real_node():
            parent_node = curr_node
            if key > parent_node.key:
                curr_node = parent_node.right
            else:
                curr_node = parent_node.left
            parent_node.size += 1

        if self.root.size == 0:   # first insertion
            self.root = new_node
            new_node.set_size(1)
        elif key > parent_node.key:
            parent_node.right = new_node
            new_node.size += 1
        else:
            parent_node.left = new_node
            new_node.size += 1

        new_node.parent = parent_node
        new_node.create_virtuals()
        new_node.set_height(0)
        new_node.set_bf()

        cnt_rebalanced, did_rotation, fixing_pointer = self.fixing_after_insertion(new_node)
        # update heights and balance factor after insert new node
        self.update(did_rotation, fixing_pointer)

        return cnt_rebalanced


    """check if tree is unbalanced after delete node or after split the tree"""

    def fixing_after_deletion(self, del_node):              # O(log(n))
        # calculate height and balance factor
        curr_node = del_node
        cnt_rebalanced = 0
        did_rotation = False
        fixing_pointer = del_node

        while curr_node.is_real_node():
            prev_height = curr_node.height
            self.calc_height(curr_node)
            self.calc_size(curr_node)
            did_rotation = False

            # find bf criminal and rotate the subtree if necessary
            if -2 < curr_node.balance_factor < 2:
                if prev_height == curr_node.height:
                    break
                else:
                    cnt_rebalanced += 1
                    curr_node = curr_node.parent
                    continue
            elif curr_node.balance_factor == 2:
                did_rotation = True
                if curr_node.left.balance_factor == 1 or curr_node.left.balance_factor == 0:
                    fixing_pointer = curr_node.left
                    self.rotate(curr_node, 'right')
                    cnt_rebalanced += 1
                    curr_node = curr_node.parent
                    self.update(did_rotation, fixing_pointer)
                    continue
                else:
                    fixing_pointer = curr_node.left.right
                    self.rotate(curr_node.left, 'left')
                    self.rotate(curr_node, 'right')
                    cnt_rebalanced += 2
                    curr_node = curr_node.parent
                    self.update(did_rotation, fixing_pointer)
                    continue

            else:
                # curr_node.balance_factor == -2
                did_rotation = True
                if curr_node.right.balance_factor == -1 or curr_node.right.balance_factor == 0:
                    fixing_pointer = curr_node.right
                    self.rotate(curr_node, 'left')
                    cnt_rebalanced += 1
                    curr_node = curr_node.parent
                    self.update(did_rotation, fixing_pointer)
                    continue
                else:
                    fixing_pointer = curr_node.right.left
                    self.rotate(curr_node.right, 'right')
                    self.rotate(curr_node, 'left')
                    cnt_rebalanced += 2
                    curr_node = curr_node.parent
                    self.update(did_rotation, fixing_pointer)
                    continue

        return cnt_rebalanced, did_rotation, fixing_pointer


    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):            # O(log(n))
        successor = None
        if node.left.is_real_node() and node.right.is_real_node():
            # i.e node has two sons, replace node with the successor and delete the successor
            successor = self.successor(node)
            original_node = node
            node = successor

        parent = node.parent
        if node.right.is_real_node():
            son = node.right
        else:
            son = node.left

        son.parent = parent
        if parent.is_real_node():
            if parent.key <= node.key:
                parent.right = son
            else:
                parent.left = son
        else:       # when delete root
            self.root = son

        if successor is not None:
            original_node.key = successor.key
            original_node.value = successor.value

        cnt_rebalanced, did_rotation, fixing_pointer = self.fixing_after_deletion(parent)
        # update heights and balance factor after delete
        self.update(did_rotation, fixing_pointer)

        return cnt_rebalanced

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """
    def avl_to_array(self):              # O(n)
        node_array = []
        # create pointer to min in tree
        node = AVLTree.get_min(self, self.root)
        length = self.size()
        node_array.append((node.key, node.value))
        if length == 0:
            return []

        for i in range(length-1):
            # call successor lengths time
            successor = AVLTree.successor(self, node)
            if successor is None:
                break
            node_array.append((successor.key, successor.value))
            node = successor

        return node_array

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """
    def size(self):              # O(1)
        return self.root.size

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):                 # O(log(n))
        smaller_tree = AVLTree()
        bigger_tree = AVLTree()
        smaller_tree.root = node.left
        bigger_tree.root = node.right

        curr_node = node
        while curr_node.parent.is_real_node():
            join_node = curr_node.parent
            tmp_tree = AVLTree()
            if join_node.key > curr_node.key:
                tmp_tree.root = join_node.right
                tmp_tree.root.parent = AVLNode(None, None)
                bigger_tree.join(tmp_tree, join_node.key, join_node.value)

            else:
                tmp_tree.root = join_node.left
                tmp_tree.root.parent = AVLNode(None, None)
                smaller_tree.join(tmp_tree, join_node.key, join_node.value)

            curr_node = join_node
            self.root = AVLNode(None, None)    # self is no more available

        return [smaller_tree, bigger_tree]

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separting self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def join(self, tree, key, val):                # O(log(n))
        joined_through_node = AVLNode(key, val)
        tree_height = tree.root.height
        self_height = self.root.height

        higher = tree if tree_height >= self_height else self
        lower = tree if tree_height < self_height else self
        delta = higher.root.height - lower.root.height + 1

        if higher.root.is_real_node() and higher.root.key > key:
            traverse_side = "left"
            connect_node = "right"
        else:
            traverse_side = "right"
            connect_node = "left"

        setattr(joined_through_node, traverse_side, lower.root)        # connect to smaller_keys_tree
        lower.root.parent = joined_through_node
        curr_bigger_tree_node = higher.root

        while lower.root.height < curr_bigger_tree_node.height and getattr(curr_bigger_tree_node, traverse_side).is_real_node():
            curr_bigger_tree_node = getattr(curr_bigger_tree_node, traverse_side)

        setattr(joined_through_node, connect_node, curr_bigger_tree_node)    # connect to bigger_keys_tree
        tmp = curr_bigger_tree_node.parent
        curr_bigger_tree_node.parent = joined_through_node
        if tmp.is_real_node():
            setattr(tmp, traverse_side, joined_through_node)
        joined_through_node.parent = tmp

        curr_node = joined_through_node
        self.root = higher.root if joined_through_node.parent.is_real_node() else joined_through_node
        self.calc_size(self.root)
        cnt_rebalanced, did_rotation, fixing_pointer = self.fixing_after_deletion(curr_node)
        self.update(did_rotation, fixing_pointer)

        return delta

    """compute the rank of node in the self

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """
    def rank(self, node):              # O(log(n))
        curr_node = node
        rank = node.left.size + 1

        while curr_node != self.root:
            if curr_node.key > curr_node.parent.key:
                # continue adding while there is a smaller key
                rank += curr_node.parent.left.size + 1
                curr_node = curr_node.parent
            else:
                # skip if parent's key is bigger
                curr_node = curr_node.parent

        if curr_node.key > self.root.key:
            rank += self.root.left.size

        return rank

    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """
    def select(self, i):              # O(log(n))
        curr_node = self.root
        while curr_node.is_real_node():
            r = curr_node.left.size + 1
            if i == r:
                return curr_node
            elif i < r:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
                i -= r

        return curr_node

    """returns the root of the tree representing the dictionary
    
    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """
    def get_root(self):              # O(1)
        return self.root if self.root.is_real_node() else None

    def get_min(self, node):           # O(log(n))
        curr_node = node
        while curr_node.is_real_node():
            curr_node = curr_node.left
        return curr_node.parent

    def successor(self, node):            # O(log(n))
        node = node
        if node.right.is_real_node():
            return self.get_min(node.right)
        else:
            parent = node.parent
            while parent.is_real_node() and parent.key < node.key:
                node = parent
                parent = node.parent
        return parent

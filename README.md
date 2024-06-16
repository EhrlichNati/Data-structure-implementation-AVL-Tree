# AVL Tree Implementation

## Overview

This project implements an AVL tree, a self-balancing binary search tree, in Python. The AVL tree ensures that the height of the tree remains balanced, which guarantees O(log n) time complexity for insertion, deletion, and search operations.

## Contributors

- **Username**: sheerofer
- **Username**: EhrlichNati



## Table of Contents

1. [AVLNode Class](#avlnode-class)
   - [Constructor](#constructor)
   - [Getters](#getters)
   - [Setters](#setters)
   - [Utility Methods](#utility-methods)
2. [AVLTree Class](#avltree-class)
   - [Constructor](#constructor-1)
   - [Tree Operations](#tree-operations)
   - [Balancing Methods](#balancing-methods)
   - [Utility Methods](#utility-methods-1)

## AVLNode Class

A class representing a node in an AVL tree.

### Constructor

```python
class AVLNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.balance_factor = None
        self.height = -1
        self.size = 0

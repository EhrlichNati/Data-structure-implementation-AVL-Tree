# AVL Tree Implementation

## Overview

This project implements an AVL tree, a self-balancing binary search tree, in Python. The AVL tree ensures that the height of the tree remains balanced, which guarantees O(log n) time complexity for insertion, deletion, and search operations.

## Contributors

- **Username**: EhrlichNati
- **Username**: sheerofer

## Table of Contents

1. [AVLNode Class](#avlnode-class)
   - [Constructor](#constructor)
   - [Getters and Setters](#getters-and-setters)
   - [Utility Methods](#utility-methods)
2. [AVLTree Class](#avltree-class)
   - [Constructor](#constructor-1)
   - [Tree Operations](#tree-operations)
   - [Balancing Methods](#balancing-methods)
   - [Utility Methods](#utility-methods-1)

## AVLNode Class

A class representing a node in an AVL tree.

### Layout

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


Operations ________________________________________________________________________________

def search(self, key):

def insert(self, key, val):
    
def delete(self, node):
    
def avl_to_array(self):
   
def size(self):


Getters ______________________________________________________________________________
def get_key(self):
    return self.key if self.is_real_node() else None

def get_value(self):
    return self.value if self.is_real_node() else None

def get_left(self):
    return self.left if self.is_real_node() else None

def get_right(self):
    return self.right if self.is_real_node() else None

def get_parent(self):
    return self.parent if self.parent.is_real_node() else None

def get_height(self):
    return self.height if self.is_real_node() else -1

def get_size(self):
    return self.size if self.is_real_node() else 0

Setters ________________________________________________________________________________

def set_key(self, key):
    self.key = key

def set_value(self, value):
    self.value = value

def set_left(self, node):
    self.left = node

def set_right(self, node):
    self.right = node

def set_parent(self, node):
    self.parent = node

def set_height(self, h):
    self.height = h

def set_size(self, s):
    self.size = s


   





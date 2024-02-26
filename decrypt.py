REVERSE = """The following is the decryption function.
```python
def decryption(encrypted_problem):
    # reverse the sentence to get original problem
    original_problem = ' '.join(encrypted_problem.split(' ')[::-1])

    return original_problem
```
"""

BINARY_TREE = """
The follwing is the decryption function.
```python
import json

class TreeNode:
    '''A node in the binary tree.'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def string_to_tree(problem_description):
    '''Converts a JSON string representation of a tree back to a tree data structure.'''
    def helper(node_dict):
        if node_dict is None:
            return None
        node = TreeNode(node_dict['value'])
        node.left = helper(json.loads(node_dict['left'])) if node_dict['left'] else None
        node.right = helper(json.loads(node_dict['right'])) if node_dict['right'] else None
        return node

    return helper(json.loads(problem_description))

def inorder_traversal(node, words):
    '''Performs inorder traversal of the tree and collects the words.'''
    if node is not None:
        inorder_traversal(node.left, words)
        words.append(node.value)
        inorder_traversal(node.right, words)

# This is the decryption function
def decryption(encrypted_problem):
    tree_root = string_to_tree(encrypted_problem)
    words = []
    inorder_traversal(tree_root, words)
    original_problem = ' '.join(words)

    return original_problem
```
"""

ODD_EVEN = """
The following is the decryption function.
```python
def decryption(encrypted_problem):
    # split sentence in half
    words = encrypted_problem.split()
    half_length = (len(words) + 1) // 2
    decrypted_words = []

    # Place the first half in an odd numbered position
    # Put the last half in an even number position
    for i in range(half_length):
        decrypted_words.append(words[i])
        if i + half_length < len(words):
            decrypted_words.append(words[i + half_length])

    original_problem = ' '.join(decrypted_words)
    return original_problem
```
"""

LENGTH = """
The following is the decryption function.
```python
def decryption(encrypted_problem):
    # Create an empty sentence
    sentence = [''] * len(encrypted_problem)
    # Iterate through the list and place each word at the correct position
    for word_dict in encrypted_problem:
        for word, index in word_dict.items():
            sentence[index] = word
    # Join the list of words to get the original problem
    original_problem = ' '.join(sentence)
    return original_problem
```
"""
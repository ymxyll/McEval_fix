

def preorder_traversal(inorder: str, postorder: str) -> str:
    """
    Reconstructs the binary tree from its inorder and postorder traversals and
    returns the preorder traversal as a string.

    Args:
    inorder (str): The inorder traversal of the binary tree.
    postorder (str): The postorder traversal of the binary tree.

    Returns:
    str: The preorder traversal of the binary tree.

    Cases:
    - If both inorder and postorder traversals are empty, returns an empty string.
    - If the tree consists of a single node, returns a string with that single node.
    - For a larger tree, recursively finds the root from the postorder traversal,
      splits the inorder traversal into left and right subtrees, and constructs
      the preorder traversal by visiting the root followed by the left and right
      subtrees.

    Example:
    - Given inorder traversal 'BADC' and postorder traversal 'BDCA', the function
      will return the preorder traversal 'ABCD'.
    - Given inorder traversal 'DBGEACF' and postorder traversal 'DGEBFCA', the function
      will return the preorder traversal 'ABDEGCF'.
    - Given a tree with a single node represented by the inorder and postorder traversal 'A',
      the function will return 'A'.
    """
    # Base case: if the traversals are empty, return an empty string
    if not inorder or not postorder:
        return ""
    
    # The root is always the last element in postorder traversal
    root = postorder[-1]
    
    # Index of root in inorder traversal
    root_index = inorder.index(root)
    
    # Recursively find the preorder traversal
    # Left subtree: from start to root_index in inorder, and the corresponding elements in postorder
    # Right subtree: from root_index + 1 to end in inorder, and the corresponding elements in postorder
    # Note: The corresponding elements in postorder are found by excluding the last element (root) and adjusting the length
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index:-1]
    
    # Construct the preorder traversal: root + left subtree + right subtree
    return root + preorder_traversal(left_inorder, left_postorder) + preorder_traversal(right_inorder, right_postorder)
def test_preorder_traversal():
    # Test case 1
    inorder1 = "BADC"
    postorder1 = "BDCA"
    expected_preorder1 = "ABCD"
    assert preorder_traversal(inorder1, postorder1) == expected_preorder1
    print(f"Test case 1 passed. Preorder: {preorder_traversal(inorder1, postorder1)}")

    # Test case 2
    inorder2 = "DBGEACF"
    postorder2 = "DGEBFCA"
    expected_preorder2 = "ABDEGCF"
    assert preorder_traversal(inorder2, postorder2) == expected_preorder2
    print(f"Test case 2 passed. Preorder: {preorder_traversal(inorder2, postorder2)}")

    # Test case 3
    inorder3 = "A"
    postorder3 = "A"
    expected_preorder3 = "A"
    assert preorder_traversal(inorder3, postorder3) == expected_preorder3
    print(f"Test case 3 passed. Preorder: {preorder_traversal(inorder3, postorder3)}")

# Run the test function
test_preorder_traversal()
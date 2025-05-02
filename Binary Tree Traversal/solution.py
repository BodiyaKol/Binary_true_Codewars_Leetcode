# Pre-order traversal
def pre_order(node):
    if not node:
        return []
    list_of_visited = []
    stack = [node]
    while stack:
        cur = stack.pop()
        list_of_visited.append(cur.data)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return list_of_visited

# In-order traversal
def in_order(node):
    list_of_visited = []
    stack = []
    cur = node
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        list_of_visited.append(cur.data)
        cur = cur.right
    return list_of_visited

# Post-order traversal
def post_order(node):
    if not node:
        return []
    list_of_visited = []
    stack1 = [node]
    stack2 = []
    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
    while stack2:
        list_of_visited.append(stack2.pop().data)
    return list_of_visited

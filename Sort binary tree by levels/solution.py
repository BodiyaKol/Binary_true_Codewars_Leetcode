def tree_by_levels(node):
    if not node:
        return []
    
    result = []
    queue = [node]
    i = 0
    
    while i < len(queue):
        cur = queue[i]
        result.append(cur.value)
        if current.left:
            queue.append(cur.left)
        if current.right:
            queue.append(cur.right)
        i += 1
    
    return result

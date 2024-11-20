from collections import deque

def DFS(a, b, target):
    # Map to store visited states
    visited = {}
    is_solvable = False
    path = []
    
    # Queue for BFS/DFS
    q = deque()
    q.append((0, 0))  # Initial state with both jugs empty

    while q:
        u = q.popleft()  # Current state
        
        # Skip if already visited
        if (u[0], u[1]) in visited:
            continue
        
        # If out of bounds, skip
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        # Mark state as visited
        visited[(u[0], u[1])] = True

        # Add state to path
        path.append([u[0], u[1]])

        # Check if target is reached
        if u[0] == target or u[1] == target:
            is_solvable = True
            if u[0] == target and u[1] != 0:
                path.append([u[0], 0])
            elif u[1] == target and u[0] != 0:
                path.append([0, u[1]])

            # Print the solution path
            for p in path:
                print(f"({p[0]}, {p[1]})")
            break

        # Generate all possible next states
        q.append((u[0], b))  # Fill Jug2
        q.append((a, u[1]))  # Fill Jug1
        q.append((0, u[1]))  # Empty Jug1
        q.append((u[0], 0))  # Empty Jug2

        # Pour water from Jug1 to Jug2
        pour_to_b = min(u[0], b - u[1])
        q.append((u[0] - pour_to_b, u[1] + pour_to_b))

        # Pour water from Jug2 to Jug1
        pour_to_a = min(u[1], a - u[0])
        q.append((u[0] + pour_to_a, u[1] - pour_to_a))
    
    if not is_solvable:
        print("No solution")

# Test case
Jug1, Jug2, target = 4, 3, 2
print("Path from initial state to solution state:")
DFS(Jug1, Jug2, target)

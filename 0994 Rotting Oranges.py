from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize Queue with all originally rotten oranges
        # and count fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # Edge case: No fresh oranges implies 0 minutes needed
        if fresh_count == 0:
            return 0
        
        minutes = 0
        
        # Step 2: Multi-source BFS
        while queue and fresh_count > 0:
            minutes += 1
            # Process strictly the number of elements currently in queue (current level)
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check bounds and if it is a fresh orange
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # Mark as rotten
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        # Step 3: Check if any fresh oranges remain
        return minutes if fresh_count == 0 else -1
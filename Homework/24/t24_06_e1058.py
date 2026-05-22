import os
import time
from collections import deque


WALL_CHAR = "*"  # WALL
CELL_CHAR = "·"  # NOT WALL



class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.m = len(maze[0])
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


    def mark_lake(self, si, sj, num):

        if isinstance(self.maze[si][sj], int):
            return 0

        count = 0
        queue = deque()

        queue.append((si, sj))
        while queue:
            i, j = queue.popleft()
            count += 1
            self.maze[i][j] = num


            for di, dj in self.directions:
                ni, nj = i + di, j + dj
                if not(0 <= ni < self.n and 0 <= nj < self.m):
                    continue 

                if not isinstance(self.maze[ni][nj], int) and self.maze[ni][nj] == CELL_CHAR:
                    self.maze[ni][nj] = num
                    queue.append((ni, nj))


        return count


if __name__ == "__main__":
    # time.sleep(2)
    with open("input.txt") as f:
        N, M, K = map(int, f.readline().split())

        maze_matrix = [
            [WALL_CHAR] * M for _ in range(N)
        ]
        submerged = []
        for _ in range(K):
            i,j = map(lambda x: int(x) - 1, f.readline().split())
            maze_matrix[i][j] = CELL_CHAR
            submerged.append((i,j))

        maze = Maze(maze_matrix)
        _max = 0
        for i in range(K):
            cell = submerged[i]
            _max = max(maze.mark_lake(*cell, i), _max)
        print(_max)

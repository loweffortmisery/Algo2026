import os
import time
from collections import deque

# Константи для стану клітинок
EMPTY = 0
VISITED = 1

# Символи для відображення в консолі
WALL_CHAR = "*"  # Стіна
CELL_CHAR = "·"  # Недосліджена клітинка
VISITED_CHAR = "▒"  # Досліджена клітинка
CURRENT_CHAR = "@"  # Поточна клітинка в обробці


class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.n = len(maze)
        self.directions = ((1, 0), (0, 1), (-1, 0), (0, -1))



    def bfs_count_wall_area(self, si, sj, fi, fj):
        wave_matrix = [[EMPTY] * self.n for _ in range(self.n)]
        count = 0
        queue = deque()

        queue.append((si, sj))
        wave_matrix[si][sj] = VISITED
        queue.append((fi, fj))
        wave_matrix[fi][fj] = VISITED
        while queue:
            i, j = queue.popleft()


            for di, dj in self.directions:
                ni, nj = i + di, j + dj

                # Перевірка меж та стану
                if self.maze[ni][nj] == "#":
                    count += 1
                    continue

                if self.maze[ni][nj] == "." and wave_matrix[ni][nj] == EMPTY:
                    wave_matrix[ni][nj] = VISITED
                    queue.append((ni, nj))


        return count-4



if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        maze_matrix = [
            ['#'] * (n+2),
            *[list('#' + f.readline().strip() + '#') for _ in range(n)],
            ['#'] * (n+2)
        ]

        maze = Maze(maze_matrix)
        print((maze.bfs_count_wall_area(1, 1, n, n))*9)

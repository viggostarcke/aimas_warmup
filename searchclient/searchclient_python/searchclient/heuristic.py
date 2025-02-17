import collections
from abc import ABC, abstractmethod

from searchclient.state import State
from searchclient.color import Color



class Heuristic(ABC):
    def __init__(self, initial_state: State) -> None:
        self.rows = len(initial_state.walls)
        self.cols = len(initial_state.walls[0])
        self.box_goals = []  # list of box goals: (goal_row, goal_col, goal_letter)
        for row_idx, row in enumerate(initial_state.goals):
            for col_idx, cell in enumerate(row):
                if cell.isalpha() and cell.isupper():
                    self.box_goals.append((row_idx, col_idx, cell))

        self.goal_dist_maps = {}  # dict: (goal_row, goal_col) -> 2D list of distances
        for (goal_row, goal_col, _) in self.box_goals:
            self.goal_dist_maps[(goal_row, goal_col)] = self._compute_manhattan_dist_map(goal_row, goal_col)


        self.agent_colors = initial_state.agent_colors
        self.box_colors = {(r, c): initial_state.box_colors[ord(initial_state.boxes[r][c]) - ord('A')]
                           for r in range(self.rows) for c in range(self.cols) if initial_state.boxes[r][c]}

        self.color_priorities = {color: idx for idx, color in enumerate(Color)}
        # self.agent_colors = initial_state.agent_colors
        # self.box_colors = {(r, c): initial_state.box_colors[r][c] for r in range(self.rows) for c in range(self.cols) if initial_state.boxes[r][c]}
        # self.color_priorities = {color: idx for idx, color in enumerate(Color)}
    def _compute_manhattan_dist_map(self, goal_row, goal_col):
        return [[abs(row - goal_row) + abs(col - goal_col) for col in range(self.cols)]
                for row in range(self.rows)]

    def _compute_bfs_dist_map(self, state: State, goal_row, goal_col):
        distance = [[float('inf')] * self.cols for _ in range(self.rows)]
        queue = collections.deque()

        distance[goal_row][goal_col] = 0
        queue.append((goal_row, goal_col))

        while queue:
            row, col = queue.popleft()
            dist = distance[row][col]
            for dist_row, dist_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_row, neighbor_col = row + dist_row, col + dist_col
                if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
                    if not state.walls[neighbor_row][neighbor_col]:
                        if distance[neighbor_row][neighbor_col] > dist + 1:
                            distance[neighbor_row][neighbor_col] = dist + 1
                            queue.append((neighbor_row, neighbor_col))

        return distance


    def h(self, state: State) -> int:
        total_distance = 0

        for (goal_row, goal_col, goal_letter) in self.box_goals:
            for row in range(self.rows):
                for col in range(self.cols):
                    if state.boxes[row][col] == goal_letter:
                        dist = self.goal_dist_maps[(goal_row, goal_col)][row][col]
                        total_distance += dist

        for agent_id, (agent_r, agent_c) in enumerate(zip(state.agent_rows, state.agent_cols)):
            agent_color = self.agent_colors[agent_id]
            agent_priority = self.color_priorities.get(agent_color, float('inf')) if agent_color else float('inf')
            min_dist = float('inf')

            for (r, c), box_color in self.box_colors.items():
                if box_color == agent_color:
                    dist = abs(agent_r - r) + abs(agent_c - c)

                    weighted_dist = dist - (agent_priority * 0.1)  # Higher priority agents get slight advantage
                    min_dist = min(min_dist, weighted_dist) + 1
            if min_dist != float('inf'):
                total_distance += min_dist
        return total_distance

    @abstractmethod
    def f(self, state: State) -> int: ...

    @abstractmethod
    def __repr__(self) -> str: ...


class HeuristicAStar(Heuristic):
    def __init__(self, initial_state: State) -> None:
        super().__init__(initial_state)

    def f(self, state: State) -> int:
        return state.g + self.h(state)

    def __repr__(self) -> str:
        return "A* evaluation"


class HeuristicWeightedAStar(Heuristic):
    def __init__(self, initial_state: State, w: int) -> None:
        super().__init__(initial_state)
        self.w = w

    def f(self, state: State) -> int:
        return state.g + self.w * self.h(state)

    def __repr__(self) -> str:
        return f"WA*({self.w}) evaluation"


class HeuristicGreedy(Heuristic):
    def __init__(self, initial_state: State) -> None:
        super().__init__(initial_state)

    def f(self, state: State) -> int:
        return self.h(state)

    def __repr__(self) -> str:
        return "greedy evaluation"

# GoalCount:
#   def __init__(self, initial_state: State) -> None:
#       self.goals = {}  # dict: agent id -> (goal_row_idx, goal_col_idx)
#       for row_idx, row in enumerate(State.goals):
#           for col_idx, cell in enumerate(row):
#               if cell.isdigit():
#                   agent_id = int(cell)
#                   self.goals[agent_id] = (row_idx, col_idx)
#
#   def h(self, state: State) -> int:
#       goal_count = 0
#       for agent_id, (goal_row, goal_col) in self.goals.items():
#           curr_row = state.agent_rows[agent_id]
#           curr_col = state.agent_cols[agent_id]
#           if (curr_row, curr_col) != (goal_row, goal_col):
#               goal_count += 1
#
#       return goal_count

# ManhattanDist:
#   def __init__(self, initial_state: State) -> None:
#       self.goals = {}  # dict: agent id -> (goal_row_idx, goal_col_idx)
#       for row_idx, row in enumerate(initial_state.goals):
#           for col_idx, cell in enumerate(row):
#               if cell.isdigit():
#                   agent_id = int(cell)
#                   self.goals[agent_id] = (row_idx, col_idx)
#
#   def h(self, state: State) -> int:
#       summed_manhattan_dist = 0
#       for agent, (goal_row, goal_col) in self.goals.items():
#           curr_row = state.agent_rows[agent]
#           curr_col = state.agent_cols[agent]
#           summed_manhattan_dist += abs(curr_row - goal_row) + abs(curr_col - goal_col)
#
#       return summed_manhattan_dist

# DistMap:
#     def __init__(self, initial_state: State) -> None:
#         self.goals = {}  # dict: agent id -> (goal_row_idx, goal_col_idx)
#         for row_idx, row in enumerate(initial_state.goals):
#             for col_idx, cell in enumerate(row):
#                 if cell.isdigit():
#                     agent_id = int(cell)
#                     self.goals[agent_id] = (row_idx, col_idx)
#
#         self.rows = len(initial_state.walls[0])
#         self.cols = len(initial_state.walls[1])
#         self.dist_maps = {}  # dict: agent id -> 2D list of distances
#         for agent, (goal_row, goal_col) in self.goals.items():
#             self.dist_maps[agent] = self._compute_bfs_dist_map(goal_row, goal_col)
#
#     def _compute_bfs_dist_map(self, goal_row: int, goal_col: int):
#         """ compute a 2D dist map: every cell shows dist to goal using bfs. """
#         distance = [[float('inf')] * self.cols for _ in range(self.rows)]
#         queue = collections.deque()
#         distance[goal_row][goal_col] = 0
#         queue.append((goal_row, goal_col))
#         while queue:
#             row, col = queue.popleft()
#             dist = distance[row][col]
#             for dist_row, dist_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 neighbor_row, neighbor_col = row + dist_row, col + dist_col
#                 if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
#                     if not State.walls[neighbor_row][neighbor_col]:
#                         if distance[neighbor_row][neighbor_col] > dist + 1:
#                             distance[neighbor_row][neighbor_col] = dist + 1
#                             queue.append((neighbor_row, neighbor_col))
#
#         return distance
#
#     def h(self, state: State) -> int:
#         """ return the max of every agents placement in the dist maps.
#         i.e. the distance of the agent which has the longest route to goal """
#         max_dist = 0
#         for agent, dist_map in self.dist_maps.items():
#             curr_row = state.agent_rows[agent]
#             curr_col = state.agent_cols[agent]
#             dist = dist_map[curr_row][curr_col]
#             if dist > max_dist:
#                 max_dist = dist
#
#         return max_dist

# GoalCount boxes:
#     def __init__(self, initial_state: State) -> None:
#         self.box_goals = []  # list of box goals: (goal_row, goal_col, letter)
#         for row_idx, row in enumerate(initial_state.goals):
#             for col_idx, cell in enumerate(row):
#                 if cell.isalpha() and cell.isupper():
#                     self.box_goals.append((row_idx, col_idx, cell))
#
#     def h(self, state: State) -> int:
#         goal_count = 0
#         for (goal_row, goal_col, letter) in self.box_goals:
#             if state.boxes[goal_row][goal_col] != letter:
#                 goal_count += 1
#
#         return goal_count

# DistMap boxes:
# def __init__(self, initial_state: State) -> None:
#     self.rows = len(initial_state.walls)
#     self.cols = len(initial_state.walls[0])
#     self.box_goals = []  # list of box goals: (goal_row, goal_col, goal_letter)
#     for row_idx, row in enumerate(initial_state.goals):
#         for col_idx, cell in enumerate(row):
#             if cell.isalpha() and cell.isupper():
#                 self.box_goals.append((row_idx, col_idx, cell))
#
#     self.goal_dist_maps = {}  # dict: (goal_row, goal_col) -> 2D list of distances
#     for (goal_row, goal_col, _) in self.box_goals:
#         self.goal_dist_maps[(goal_row, goal_col)] = self._compute_bfs_dist_map(initial_state, goal_row, goal_col)
#
#
# def _compute_bfs_dist_map(self, state: State, goal_row, goal_col):
#     distance = [[float('inf')] * self.cols for _ in range(self.rows)]
#     queue = collections.deque()
#
#     distance[goal_row][goal_col] = 0
#     queue.append((goal_row, goal_col))
#
#     while queue:
#         row, col = queue.popleft()
#         dist = distance[row][col]
#         for dist_row, dist_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             neighbor_row, neighbor_col = row + dist_row, col + dist_col
#             if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols:
#                 if not state.walls[neighbor_row][neighbor_col]:
#                     if distance[neighbor_row][neighbor_col] > dist + 1:
#                         distance[neighbor_row][neighbor_col] = dist + 1
#                         queue.append((neighbor_row, neighbor_col))
#
#     return distance
#
#
# def h(self, state: State) -> int:
#     total_distance = 0
#
#     for (goal_row, goal_col, goal_letter) in self.box_goals:
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 if state.boxes[row][col] == goal_letter:
#                     dist = self.goal_dist_maps[(goal_row, goal_col)][row][col]
#                     total_distance += dist
#
#     return total_distance
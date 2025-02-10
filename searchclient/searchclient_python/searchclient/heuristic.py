import collections
from abc import ABC, abstractmethod

from searchclient.state import State


class Heuristic(ABC):
    def __init__(self, initial_state: State) -> None:
        self.goals = {}  # dict: agent id -> (goal_row_idx, goal_col_idx)
        for row_idx, row in enumerate(initial_state.goals):
            for col_idx, cell in enumerate(row):
                if cell.isdigit():
                    agent_id = int(cell)
                    self.goals[agent_id] = (row_idx, col_idx)

        self.rows = len(initial_state.walls[0])
        self.cols = len(initial_state.walls[1])
        self.dist_maps = {}  # dict: agent id -> 2D list of distances
        for agent, (goal_row, goal_col) in self.goals.items():
            self.dist_maps[agent] = self._compute_bfs_dist_map(goal_row, goal_col)

    def _compute_bfs_dist_map(self, goal_row: int, goal_col: int):
        """ compute a 2D dist map: every cell shows dist to goal using bfs. """
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
                    if not State.walls[neighbor_row][neighbor_col]:
                        if distance[neighbor_row][neighbor_col] > dist + 1:
                            distance[neighbor_row][neighbor_col] = dist + 1
                            queue.append((neighbor_row, neighbor_col))

        return distance

    def h(self, state: State) -> int:
        """ return the max of every agents placement in the dist maps.
        i.e. the distance of the agent which has the longest route to goal """
        distances = []
        for agent, dist_map in self.dist_maps.items():
            curr_row = state.agent_rows[agent]
            curr_col = state.agent_cols[agent]
            distances.append(dist_map[curr_row][curr_col])
        if not distances:
            return 0
        return max(distances)

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
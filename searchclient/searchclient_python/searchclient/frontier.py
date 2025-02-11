import heapq
from abc import ABC, abstractmethod
from collections import deque

from searchclient.heuristic import Heuristic
from searchclient.state import State


class Frontier(ABC):
    @abstractmethod
    def add(self, state: State) -> None: ...

    @abstractmethod
    def pop(self) -> State: ...

    @abstractmethod
    def is_empty(self) -> bool: ...

    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def contains(self, state: State) -> bool: ...

    @abstractmethod
    def get_name(self) -> str: ...


class FrontierBFS(Frontier):
    def __init__(self) -> None:
        super().__init__()
        self.queue: deque[State] = deque()
        self.set: set[State] = set()

    def add(self, state: State) -> None:
        self.queue.append(state)
        self.set.add(state)

    def pop(self) -> State:
        state = self.queue.popleft()
        self.set.remove(state)
        return state

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def size(self) -> int:
        return len(self.queue)

    def contains(self, state: State) -> bool:
        return state in self.set

    def get_name(self) -> str:
        return "breadth-first search"


class FrontierDFS(Frontier):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[State] = [] # LIFO stack for DFS
        self.set: set[State] = set() # set of states in the frontier

    def add(self, state: State) -> None:
        """Add a state to the frontier."""
        self.stack.append(state) # add to the end of the list
        self.set.add(state) # add to the set

    def pop(self) -> State:
        """Remove the last state in the frontier and return it."""
        state = self.stack.pop() # choose the last state in the list
        self.set.remove(state) # remove from the set
        return state

    def is_empty(self) -> bool:
        """Check if the frontier is empty"""
        return len(self.stack) == 0 

    def size(self) -> int:
        """Return the size of the frontier"""
        return len(self.stack)

    def contains(self, state: State) -> bool:
        """Check if the frontier contains a given state"""
        return state in self.set

    def get_name(self) -> str:
        return "depth-first search"


class FrontierBestFirst(Frontier):
    def __init__(self, heuristic: Heuristic) -> None:
        super().__init__()
        self.heuristic = heuristic
        self.frontier = []
        self.in_frontier = set()
        self.counter = 0    #  in case two nodes have same cost

    def add(self, state: State) -> None:
        if state not in self.in_frontier:
            self.in_frontier.add(state)
            heapq.heappush(self.frontier, (self.heuristic.f(state) , self.counter, state))
            self.counter += 1

    def pop(self) -> State:
        _, _, state = heapq.heappop(self.frontier)
        self.in_frontier.remove(state)
        return state

    def is_empty(self) -> bool:
        return len(self.frontier) == 0

    def size(self) -> int:
        return len(self.frontier)

    def contains(self, state: State) -> bool:
        return state in self.in_frontier

    def get_name(self) -> str:
        return f"best-first search using {self.heuristic}"

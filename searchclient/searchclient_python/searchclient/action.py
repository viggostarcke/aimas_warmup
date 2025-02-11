from enum import Enum, unique
from typing import Literal

@unique
class ActionType(Enum):
    NoOp = 0
    Move = 1
    Push = 2
    Pull = 3


@unique
class Action(Enum):
    NoOp = ("NoOp", ActionType.NoOp, 0, 0, 0, 0)

    MoveN = ("Move(N)", ActionType.Move, -1, 0, 0, 0)
    MoveS = ("Move(S)", ActionType.Move, 1, 0, 0, 0)
    MoveE = ("Move(E)", ActionType.Move, 0, 1, 0, 0)
    MoveW = ("Move(W)", ActionType.Move, 0, -1, 0, 0)

    # Push actions: Agent moves in direction X and pushes the box in the same or a different direction Y.
    PushN = ("Push(N,N)", ActionType.Push, -1, 0, -1, 0)
    PushS = ("Push(S,S)", ActionType.Push, 1, 0, 1, 0)
    PushE = ("Push(E,E)", ActionType.Push, 0, 1, 0, 1)
    PushW = ("Push(W,W)", ActionType.Push, 0, -1, 0, -1)

    PushNE = ("Push(N,E)", ActionType.Push, -1, 0, 0, 1)
    PushNW = ("Push(N,W)", ActionType.Push, -1, 0, 0, -1)
    PushSE = ("Push(S,E)", ActionType.Push, 1, 0, 0, 1)
    PushSW = ("Push(S,W)", ActionType.Push, 1, 0, 0, -1)

    PushEN = ("Push(E,N)", ActionType.Push, 0, 1, -1, 0)
    PushES = ("Push(E,S)", ActionType.Push, 0, 1, 1, 0)
    PushWN = ("Push(W,N)", ActionType.Push, 0, -1, -1, 0)
    PushWS = ("Push(W,S)", ActionType.Push, 0, -1, 1, 0)

    # Pull actions: Agent moves in direction X and pulls a box from direction Y.
    PullN = ("Pull(N,S)", ActionType.Pull, -1, 0, 1, 0)
    PullS = ("Pull(S,N)", ActionType.Pull, 1, 0, -1, 0)
    PullE = ("Pull(E,W)", ActionType.Pull, 0, 1, 0, -1)
    PullW = ("Pull(W,E)", ActionType.Pull, 0, -1, 0, 1)

    PullNN = ("Pull(N,N)", ActionType.Pull, -1, 0, -1, 0)
    PullSS = ("Pull(S,S)", ActionType.Pull, 1, 0, 1, 0)
    PullEE = ("Pull(E,E)", ActionType.Pull, 0, 1, 0, 1)
    PullWW = ("Pull(W,W)", ActionType.Pull, 0, -1, 0, -1)

    PullNE = ("Pull(N,E)", ActionType.Pull, -1, 0, 0, 1)
    PullNW = ("Pull(N,W)", ActionType.Pull, -1, 0, 0, -1)
    PullSE = ("Pull(S,E)", ActionType.Pull, 1, 0, 0, 1)
    PullSW = ("Pull(S,W)", ActionType.Pull, 1, 0, 0, -1)

    PullEN = ("Pull(E,N)", ActionType.Pull, 0, 1, -1, 0)
    PullES = ("Pull(E,S)", ActionType.Pull, 0, 1, 1, 0)
    PullWN = ("Pull(W,N)", ActionType.Pull, 0, -1, -1, 0)
    PullWS = ("Pull(W,S)", ActionType.Pull, 0, -1, 1, 0)

    def __init__(
        self,
        name: str,
        type: ActionType,
        ard: int,
        acd: int,
        brd: int,
        bcd: int,
    ) -> None:
        self.name_ = name
        self.type = type
        self.agent_row_delta = ard  # Agent movement delta
        self.agent_col_delta = acd  # Agent movement delta
        self.box_row_delta = brd  # Box movement delta
        self.box_col_delta = bcd  # Box movement delta

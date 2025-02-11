import random
from typing import ClassVar, Optional
from searchclient.action import Action, ActionType
from searchclient.color import Color


class State:
    _RNG = random.Random(1)

    agent_colors: ClassVar[list[Optional[Color]]]
    walls: ClassVar[list[list[bool]]]
    box_colors: ClassVar[list[Optional[Color]]]
    goals: ClassVar[list[list[str]]]

    def __init__(self, agent_rows: list[int], agent_cols: list[int], boxes: list[list[Optional[str]]]) -> None:
        """
        Constructs an initial state.
        """
        self.agent_rows = agent_rows
        self.agent_cols = agent_cols
        self.boxes = boxes
        self.parent: Optional[State] = None
        self.joint_action: Optional[list[Action]] = None
        self.g = 0
        self._hash: Optional[int] = None

    def result(self, joint_action: list[Action]) -> "State":
        """
        Returns the resulting state after applying joint_action.
        Precondition: Actions must be applicable and non-conflicting.
        """
        copy_agent_rows = self.agent_rows[:]
        copy_agent_cols = self.agent_cols[:]
        copy_boxes = [row[:] for row in self.boxes]

        for agent, action in enumerate(joint_action):
            if action.type is ActionType.NoOp:
                continue

            agent_row, agent_col = copy_agent_rows[agent], copy_agent_cols[agent]

            if action.type is ActionType.Move:
                copy_agent_rows[agent] += action.agent_row_delta
                copy_agent_cols[agent] += action.agent_col_delta

            elif action.type is ActionType.Push:
                box_row, box_col = agent_row + action.agent_row_delta, agent_col + action.agent_col_delta
                new_box_row, new_box_col = box_row + action.box_row_delta, box_col + action.box_col_delta

                copy_agent_rows[agent] += action.agent_row_delta
                copy_agent_cols[agent] += action.agent_col_delta
                copy_boxes[new_box_row][new_box_col] = copy_boxes[box_row][box_col]
                copy_boxes[box_row][box_col] = None

            elif action.type is ActionType.Pull:
                box_row, box_col = agent_row - action.agent_row_delta, agent_col - action.agent_col_delta

                copy_agent_rows[agent] += action.agent_row_delta
                copy_agent_cols[agent] += action.agent_col_delta
                copy_boxes[agent_row][agent_col] = copy_boxes[box_row][box_col]
                copy_boxes[box_row][box_col] = None

        new_state = State(copy_agent_rows, copy_agent_cols, copy_boxes)
        new_state.parent = self
        new_state.joint_action = joint_action.copy()
        new_state.g = self.g + 1

        return new_state

    def is_goal_state(self) -> bool:
        """
        Checks if the current state satisfies the goal conditions.
        """
        for row in range(len(State.goals)):
            for col in range(len(State.goals[row])):
                goal = State.goals[row][col]

                if "A" <= goal <= "Z" and self.boxes[row][col] != goal:
                    return False
                if "0" <= goal <= "9" and (
                    self.agent_rows[ord(goal) - ord("0")] != row or self.agent_cols[ord(goal) - ord("0")] != col
                ):
                    return False
        return True

    def get_expanded_states(self) -> list["State"]:
        """
        Expands the state by applying all applicable actions.
        """
        num_agents = len(self.agent_rows)
        applicable_actions = [[action for action in Action if self.is_applicable(agent, action)]
                              for agent in range(num_agents)]
        print(applicable_actions)
        joint_action = [Action.NoOp] * num_agents
        actions_permutation = [0] * num_agents
        expanded_states = []

        while True:
            for agent in range(num_agents):
                joint_action[agent] = applicable_actions[agent][actions_permutation[agent]]

            if not self.is_conflicting(joint_action):
                expanded_states.append(self.result(joint_action))

            for agent in range(num_agents):
                if actions_permutation[agent] < len(applicable_actions[agent]) - 1:
                    actions_permutation[agent] += 1
                    break
                else:
                    actions_permutation[agent] = 0
                    if agent == num_agents - 1:
                        State._RNG.shuffle(expanded_states)
                        return expanded_states

    def is_applicable(self, agent: int, action: Action) -> bool:
        """
        Determines if an action is applicable in the current state.
        """
        agent_row, agent_col = self.agent_rows[agent], self.agent_cols[agent]

        if action.type is ActionType.NoOp:
            return True

        if action.type is ActionType.Move:
            return self.is_free(agent_row + action.agent_row_delta, agent_col + action.agent_col_delta)

        if action.type is ActionType.Push:
            box_row, box_col = agent_row + action.agent_row_delta, agent_col + action.agent_col_delta

            if not self.boxes[box_row][box_col]:
                return False

            return self.is_free(box_row + action.box_row_delta, box_col + action.box_col_delta)

        if action.type is ActionType.Pull:
            new_agent_row, new_agent_col = agent_row + action.agent_row_delta, agent_col + action.agent_col_delta
            box_row, box_col = agent_row - action.agent_row_delta, agent_col - action.agent_col_delta

            if not self.boxes[box_row][box_col]:
                return False

            return self.is_free(new_agent_row, new_agent_col)

        return False

    def is_conflicting(self, joint_action: list[Action]) -> bool:
        """
        Determines if joint actions create conflicts.
        """
        occupied_positions = set()

        for agent, action in enumerate(joint_action):
            agent_row, agent_col = self.agent_rows[agent], self.agent_cols[agent]

            if action.type is ActionType.NoOp:
                continue

            new_pos = (agent_row + action.agent_row_delta, agent_col + action.agent_col_delta)

            if new_pos in occupied_positions:
                return True

            occupied_positions.add(new_pos)

        return False

    def is_free(self, row: int, col: int) -> bool:
        """
        Checks if a cell is free of obstacles.
        """
        return not State.walls[row][col] and not self.boxes[row][col] and self.agent_at(row, col) is None

    def agent_at(self, row: int, col: int) -> Optional[int]:
        """
        Checks if an agent is located at a given position.
        """
        for agent in range(len(self.agent_rows)):
            if self.agent_rows[agent] == row and self.agent_cols[agent] == col:
                return agent
        return None

    def extract_plan(self) -> list[list[Action]]:
        """
        Extracts the action sequence from the initial state to this state.
        """
        plan = []
        state: Optional[State] = self

        while state is not None and state.joint_action is not None:
            plan.append(state.joint_action)
            state = state.parent

        plan.reverse()
        return plan

    def __hash__(self) -> int:
        """
        Generates a unique hash for the state.
        """
        if self._hash is None:
            self._hash = hash((tuple(self.agent_rows),
                               tuple(self.agent_cols),
                               tuple(tuple(row) for row in self.boxes)))
        return self._hash

    def __eq__(self, other: object) -> bool:
        """
        Compares two states.
        """
        if not isinstance(other, State):
            return False
        return (self.agent_rows == other.agent_rows and
                self.agent_cols == other.agent_cols and
                self.boxes == other.boxes)

    def __repr__(self) -> str:
        """
        Returns a string representation of the state.
        """
        lines = []
        for row in range(len(self.boxes)):
            line = []
            for col in range(len(self.boxes[row])):
                if self.boxes[row][col]:
                    line.append(self.boxes[row][col])
                elif State.walls[row][col]:
                    line.append("+")
                elif (agent := self.agent_at(row, col)) is not None:
                    line.append(chr(agent + ord("0")))
                else:
                    line.append(" ")
            lines.append("".join(line))
        return "\n".join(lines)

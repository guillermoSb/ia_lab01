from AgentState import AgentState
from AgentAction import AgentAction


def test_agent_cant_go_left_if_in_grid_corner():
    # Arrange
    sut = AgentState(0, 0)
    possible_actions = [AgentAction("LEFT"), AgentAction("RIGHT"), AgentAction("TOP"), AgentAction("BOTTOM")]
    # Act
    actions = sut.possible_actions(100, possible_actions)
    # Assert
    for action in actions:
        assert action.name is not "LEFT"
        assert action.name is not "TOP"

def test_agent_can_go_anywhere_if_valid():
    # Arrange
    sut = AgentState(1, 1)
    possible_actions = [AgentAction("LEFT"), AgentAction("RIGHT"), AgentAction("TOP"), AgentAction("BOTTOM")]
    # Act
    actions = sut.possible_actions(100, possible_actions)
    # Assert
    assert len(actions) == 4


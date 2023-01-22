from AgentState import AgentState
from AgentAction import AgentAction


def test_agent_moves_when_action_happens():
    # Arrange
    state = AgentState(0, 0)
    sut = AgentAction("RIGHT")
    # Act
    new_state = sut.result(state)
    # Assert
    assert new_state.x == 1


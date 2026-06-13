import re
from math import prod
from typing import TypedDict

from langgraph import StateGraph


class State(TypedDict):
    """State for the agent."""

    name: str
    values: list[int]
    operation: str
    result: str | None


def apply_operation(state: State) -> State:
    """Apply the operation to the state."""
    match state["operation"]:
        case "+":
            state["result"] = (
                f"Hello {state['name']}, your answer is {sum(state['values'])}"
            )
        case "*":
            state["result"] = (
                f"Hello {state['name']}, your answer is {prod(state['values'])}"
            )
        case _:
            raise ValueError(f"Invalid operation: {state['operation']}")

    return state


graph = StateGraph(State)

graph.add_node("apply_operation", apply_operation)

graph.set_entry_point("apply_operation")
graph.set_finish_point("apply_operation")

app = graph.compile()

result = app.invoke({"name": "Jeff", "values": [1, 2, 3], "operation": "+"})
print(result)

from typing import TypedDict

from langgraph import StateGraph


class AgentState(TypedDict):
    """State of the agent."""

    name: str


def give_compliment(state: AgentState) -> AgentState:
    """Give a compliment to the agent's name."""
    state["name"] = "Congratulations " + state["name"] + ", you are doing a great job!"
    return state


graph = StateGraph(AgentState)

graph.add_node("give_compliment", give_compliment)

graph.set_entry_point("give_compliment")
graph.set_finish_point("give_compliment")

app = graph.compile()

result = app.invoke({"name": "John"})
print(result)

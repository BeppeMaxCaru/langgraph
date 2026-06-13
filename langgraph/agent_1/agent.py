from typing import TypedDict

from langgraph import StateGraph


# Basic Agent State
class AgentState(TypedDict):
    """
    Represents the state of an agent in the LangGraph framework.
    """

    id: int
    name: str
    description: str
    roles: list


def remove_roles(state: AgentState) -> AgentState:
    state["roles"] = []
    return state


graph = StateGraph(AgentState)

graph.add_node("remove_roles", remove_roles)

graph.set_entry_point("remove_roles")
graph.set_finish_point("remove_roles")


def main():
    print("Hello from langgraph!")
    app = graph.compile()
    result = app.invoke(
        {
            "id": 0,
            "name": "LangGraph Agent",
            "description": "Agent 0, a basic agent named 'LangGraph Agent'.",
            "roles": ["Developer", "Maintainer"],
        }
    )
    print(result)


if __name__ == "__main__":
    main()

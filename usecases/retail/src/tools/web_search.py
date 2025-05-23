from ibm_watsonx_orchestrate.agent_builder.tools import ToolPermission, tool
from langchain_community.tools.tavily_search import TavilySearchResults
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.client.connections import ConnectionType

CONNECTION_TAVILY = 'tavily'

@tool(
        {"app_id": CONNECTION_TAVILY, "type": ConnectionType.KEY_VALUE}
)
def web_search(query: str) -> str:
    """Use Tavily to search the web and return the top results for a given query string."""

    tavily_api_key = connections.key_value(CONNECTION_TAVILY)['apikey']

    search = TavilySearchResults(max_results=5, tavily_api_key=tavily_api_key)
    results = search.run(query)
    return results
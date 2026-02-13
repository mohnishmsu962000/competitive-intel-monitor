import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from state import State

def web_search_node(state: State) -> dict:
    
    async def do_search():
        server_params = StdioServerParameters(
            command='npx',
            args=['-y', '@modelcontextprotocol/server-brave-search']
        )
        
        all_results = {}
        
        async with stdio_client(server_params) as (read,write):
            async with ClientSession(read, write) as session:
                    await session.initialize()
                    
                    for competitor, queries in state["research_queries"].items():
                        
                        competitor_results = []
                    
                        for query in queries:
                            result = await session.call_tool(
                                "brave_search",
                                arguments={"query": query}
                            )
                            competitor_results.append(result.content[0].text)
                        
                        all_results[competitor] = competitor_results
                    
                    return all_results
                
                
                
    results = asyncio.run(do_search())
    
    return {"search_results": results}
            
    
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command='npx',
        args=["-y", "@modelcontextprotocol/server-filesystem", "/tmp"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            tools = await session.list_tools()
            print("Available tools:", tools)
            
            result = await session.call_tool("read_file", arguments={"path": "/private/tmp/test.txt"})
            print("File content:", result)
            
    
    

if __name__ == "__main__":
    asyncio.run(main())
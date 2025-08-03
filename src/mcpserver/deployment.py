from mcp.server.fastmcp import FastMCP
import numpy as np
mcp = FastMCP("power1/4")


@mcp.tool()
def power_one_fourth(a:int) ->float:
    """ 
    Use this when user requests 1/4 power of a number or sqrt(sqrt(number))
    """
    
    a = np.sqrt(a)
    a = np.sqrt(a)
    return a

if __name__ == "__main__":
    mcp.run()
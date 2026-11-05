from fastmcp import FastMCP
import psutil


mcp = FastMCP(name="SystemStats")

@mcp.tool()
def get_system_stats():
    """
    Get system statistics including CPU usage, memory usage, and disk usage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total,
        "memory_used": memory_info.used,
        "memory_free": memory_info.free,
        "disk_total": disk_info.total,
        "disk_used": disk_info.used,
        "disk_free": disk_info.free
    }

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port="8000")
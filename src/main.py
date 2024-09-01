from appwrite.client import Client
import os

# Initialize i from environment or storage; default to 0 if not set
i = int(os.environ.get("COUNTER", 0))

def main(context):
    global i  # Ensure i is treated as a global variable
    
    # Increment i
    i += 1

    # Log the current value of i
    context.log(f"Current value of i: {i}")

    # Allow cross-origin requests
    context.res.set_header('Access-Control-Allow-Origin', '*')

    # Check if the request method is GET
    if context.req.method == "GET":
        # Set response type as plain text
        context.res.set_header('Content-Type', 'text/plain')
        return context.res.send(f"Hello, World! Current value of i: {i}")

    # For non-GET requests, set response type as JSON
    context.res.set_header('Content-Type', 'application/json')
    return context.res.json(
        {
            "motto": "Build like a team of hundreds_",
            "learn": "https://appwrite.io/docs",
            "connect": "https://appwrite.io/discord",
            "getInspired": "https://builtwith.appwrite.io",
            "counter": i
        }
    )

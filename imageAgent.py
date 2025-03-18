from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the agent
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    markdown=True,
)

# Image URL
image_url = "https://upload.wikimedia.org/wikipedia/commons/b/bf/Krakow_-_Kosciol_Mariacki.jpg"

try:
    response = agent.respond(
        "Tell me about this image and give me the latest news about it.",
        images=[image_url],
        stream=True,
    )

    # Log response
    logging.info("Response received:\n%s", response.text)

except Exception as e:
    logging.error("Error processing request: %s", str(e))

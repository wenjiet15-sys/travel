from agno.agent import Agent
from agno.tools.exa import ExaTools
from config.llm import model
import os

dining_agent = Agent(
    name="Local Dining & Cuisine Specialist",
    model=model,
    tools=[
        ExaTools(api_key=os.getenv("EXA_API_KEY"))
    ],
    instructions=[
        "# Local Dining & Cuisine Specialist",
        "",
        "## Core Task",
        "- Discover and recommend top dining options and local cuisine for the user destination.",
        "- Use the EXA tool to search for real restaurants, bistros, popular street food, and top-rated eateries.",
        "- Do NOT rely on fragile web scraping. If searching fails, rely on your internal world knowledge to recommend famous or universally acclaimed local spots.",
        "",
        "## Structure Requirements",
        "- For each restaurant, provide its name, cuisine type, estimated price range, and a brief description of its vibe and famous dishes.",
        "- YOU MUST RETURN Valid data. Do not say data is unavailable.",
        "- Group them logically (e.g. Fine Dining, Local Eats, Street Food).",
    ],
    expected_output='''
      A structured list of 4-6 restaurant recommendations with:
      - name: Restaurant name
      - cuisine: Type of food
      - price_range: e.g., , $
      - address: Rough location or neighborhood
      - description: What makes it great and signature dishes
      - url: Website or tripadvisor search link
    ''',
    markdown=True,
    debug_mode=True
)

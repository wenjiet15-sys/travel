from agno.agent import Agent
from agno.tools.exa import ExaTools
from config.llm import model
import os

hotel_search_agent = Agent(
    name="Hotel Search Assistant",
    model=model,
    tools=[
        ExaTools(api_key=os.getenv("EXA_API_KEY"))
    ],
    instructions=[
        "# Hotel Search and Data Extraction Assistant",
        "",
        "## Core Task",
        "- Search the web for actual hotel options in the user's destination using the EXA tool.",
        "- Look for high-quality blogs, booking site summaries, or review sites to find real well-known hotels.",
        "- Extract specific hotels with estimated pricing, ratings, and descriptions.",
        "",
        "## Data Generation Limits",
        "- Do NOT rely on kayak.com URL generation.",
        "- If you cannot find live accurate pricing from Exa, use your world knowledge to estimate a realistic current price based on the hotel tier (e.g. $150/night).",
        "- DO NOT FAIL. You MUST return a valid list of hotel recommendations, even if some details are estimated by you.",
        "- Include direct booking links if you find them, otherwise use generic links like https://www.booking.com or https://www.expedia.com.",
        "",
    ],
    expected_output='''
      List of 3-5 hotels with the following fields for each hotel:
      - hotel_name (str): The name of the hotel
      - price (str): The price of the hotel
      - rating (str): The rating of the hotel (e.g., 4.5/5)
      - address (str): The address or general location of the hotel
      - amenities (List[str]): 3-5 key amenities (e.g., ["Free WiFi", "Pool", "Gym"])
      - description (str): A short description of the hotel
      - url (str): A booking url or the hotel website
    ''',
    markdown=True,
    debug_mode=True,
    retries=3,
    delay_between_retries=2,
    exponential_backoff=True,
)

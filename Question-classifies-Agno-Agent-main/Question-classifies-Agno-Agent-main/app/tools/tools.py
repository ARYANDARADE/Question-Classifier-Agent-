from utils.config import config, load_env_variables
from agno.agent import Agent
from agno.team.team import Team
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from tools.prompts import get_classification_prompt, get_duckduckgo_prompt, get_tavily_prompt
from dotenv import load_dotenv
import os

load_dotenv()

env_name = load_env_variables()
tavily_api_key = os.getenv("TAVILY_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")



# Define Classifier Agent
classifier = Agent(
    name="Classifier",
    role="Classifies user questions into predefined categories",
    instructions=[
        "Analyze the user's question and classify it into one of the following categories:",
        "make sure to classify the category correctly",
        "The categories are Analytical, Theory Information, Mathematical Calculations, Statistical Inference, Differentiation, Formulation, Definition.",
        "when word define is used, return only Definition",
        "when word theory is used, return only Theory Information",
        "when word differentiate is used, return only differentiation",
        "when mathematical calculations or number or equations are used, return only Mathematical Calculations",
        "Strictly follow the instructions and categorize the question and the do further analysis.",
        "Analytical, Theory Information, Mathematical Calculations, Statistical Inference, Differentiation, Formulation, Definition.",
        "Return only the category name that best fits the question."
    ],
    system_message=get_classification_prompt(),
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o"),
    markdown=True,
    add_datetime_to_instructions=True,
)

# Define DuckDuckGo Search Agent
duckduckgo_searcher = Agent(
    name="DuckDuckGo Searcher",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o"),
    role="Searches for relevant information using DuckDuckGo",
    instructions=[
        "Given a user question, search the web using DuckDuckGo and return the most relevant results.",
        "Return a list of at most relevant response for the question."
    ],
    tools=[DuckDuckGoTools()],
    system_message=get_duckduckgo_prompt(),
    add_datetime_to_instructions=True,
)

# Define Tavily Search Agent
tavily_searcher = Agent(
    name="Tavily Searcher",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o"),
    role="Searches for relevant information using Tavily Search",
    instructions=[
        "Given a user question, search the web using Tavily Search and return the most relevant results.",
        "Return a list of at most relevant response for the question."
    ],
    tools=[TavilyTools(api_key=tavily_api_key)],
    system_message=get_tavily_prompt(),
    add_datetime_to_instructions=True,
)

# Define the Coordinator Team
orchestrator = Team(
    name="Orchestrator",
    mode="coordinate",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(api_key=openai_api_key, id="gpt-4o"),
    members=[classifier, duckduckgo_searcher, tavily_searcher],
    description="Coordinates question classification and web searches to provide a relevant answer.",
    instructions=[
        "First, ask the Classifier agent to classify the question.",
        "Then, ask the DuckDuckGo Searcher and Tavily Searcher to retrieve relevant information.",
        "Finally, return the classification followed by the retrieved information."
    ],
    add_datetime_to_instructions=True,
    show_members_responses=True,
    markdown=True,
)


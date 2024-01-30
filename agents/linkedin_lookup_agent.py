from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you
    to get it me a link to their Linkedin profile page.
    Your answer should contain only URL"""

    tools_for_agent = [Tool(name="Crawl Google 4 linkedin profile page"), func="?", description="useful when you need to get" ]
    agent = 
    return "Linkedin Profile URL"
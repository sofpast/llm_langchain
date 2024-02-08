import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

import json

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_party.linkedin import scrape_linkedin_profile
from langchain.output_parsers import PydanticOutputParser, format_instructions

information = """
Elon Reeve Musk (ilɒnEE-lon; born June 28, 1971) is a businessman and investor. He is the wealthiest person in the world, with an estimated net worth of US$222 billion as of December 2023, according to the Bloomberg Billionaires Index, and $244 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX
"""


def ice_break(name: str) -> str:
    linked_profile_url = linkedin_lookup_agent(name="Eden Macro")
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linked_profile_url)
    # print(linkedin_data)
    summary_template = """
        given the information {information} about a person from I want to you to create:
        1. a short summary
        2. Two interesting facts about them   
        3. A topic that may interest them
        4. 2 creative Ice breakers to open a conversation with them
        \n{format_instructions} 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0,
                     model_name="gpt-3.5-turbo")
    chain = LLMChain(
        llm=llm,
        prompt=summary_prompt_template
    )

    result = chain.run(linkedin_information=linkedin_data)
    print(result)
    import pdb
    pdb.set_trace()

    return result

    # with open("harrison.json", "w") as f:
    #     json.dump(linkedin_data, f, indent=4)


if __name__ == "__main__":
    print("hello langchain")
    # os.getenv('OPENAI_API_KEY')
    load_dotenv()

    result = ice_break(name="Harrison Chase")
    # print(chain.run(information=linkedin_data))

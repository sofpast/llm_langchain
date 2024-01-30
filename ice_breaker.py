import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

import json

from third_party.linkedin import scrape_linkedin_profile
information = """
Elon Reeve Musk (ilɒnEE-lon; born June 28, 1971) is a businessman and investor. He is the wealthiest person in the world, with an estimated net worth of US$222 billion as of December 2023, according to the Bloomberg Billionaires Index, and $244 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX
"""

if __name__=="__main__":
    print("hello langchain")
    # os.getenv('OPENAI_API_KEY')
    load_dotenv()

    summary_template = """
        given the information {information} about a person from I want to you to create:
        1. a short summary
        2. Two interesting facts about them    
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0,
                     model_name="gpt-3.5-turbo")
    chain = LLMChain(
        llm=llm,
        prompt=summary_prompt_template
    )
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/")
    # print(linkedin_data)
    with open("harrison.json", "w") as f:
        json.dump(linkedin_data, f, indent=4)

    print(chain.run(information=linkedin_data))



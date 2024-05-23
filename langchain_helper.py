from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv


load_dotenv()


def generate_pet_name(modification_type, car_make, car_model):
    llm = OpenAI(temperature=0.7)
    
    prompt_template_name = PromptTemplate(
        input_variables=["modification_type", "car_make", "car_model"],
        template="I just bought a {car_make} {car_model} and want to modify it. Suggest me five good {modification_type} modifications I can do.",
    
    )
    name_chain =  LLMChain(llm=llm, prompt=prompt_template_name, output_key="car_modifications")
    
    response = name_chain({'modification_type': modification_type, "car_make": car_make, "car_model": car_model})
    return response


def langchain_agent():
    llm = OpenAI(temperature=0.7)
    
    tools = load_tools(["wikipedia", "llm-math"], llm=llm)
    
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    
    result = agent.run("What is the average age of a dog? Multiple the age by 3")
    
    print(result)

if __name__ == "__main__":
    # print(generate_pet_name('exterior', 'ferrari', '458'))
    langchain_agent()
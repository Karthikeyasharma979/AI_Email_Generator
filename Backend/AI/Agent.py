from smolagents import ToolCallingAgent,LiteLLMModel
from dotenv import load_dotenv
load_dotenv()

def AI(input:str)->str:
    model = LiteLLMModel(model_id="gemini/gemini-2.0-flash")
    agent = ToolCallingAgent(model=model,tools=[])
    response = (agent.run(input))
    return response


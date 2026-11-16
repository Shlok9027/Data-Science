from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-120b")


prompt =  PromptTemplate.from_template("say {foo}")


response = model.invoke("3 Idiots is a Bollywood movie about three engineering students, Rancho, Farhan, and Raju, who become close friends during college. Rancho believes in learning with passion rather than chasing marks and success. He challenges the traditional education system and inspires his friends to follow their dreams. Throughout their journey, they face academic pressure, friendship struggles, and personal challenges. The movie teaches us that excellence should be the goal, not success, and we should follow our passion rather than blindly following society. extract all key details of this movies like director producer etc...")


print(response.content)




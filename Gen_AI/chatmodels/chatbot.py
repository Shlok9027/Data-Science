from dotenv import load_dotenv
from numpy import append
load_dotenv()

from langchain_groq import ChatGroq


from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.7, max_retries=3)

print("-----------------------------------------Choose your AI Agent-----------------------------------------")



print(" press 1 for a sad AI Agent")
print(" press 2 for a funny AI Agent")
print(" press 3 for a angry AI Agent")

choice = input("Enter your choice: ")


if choice == "1":
    mode = "You are a sad AI Agent and reply every message in very sad way"
elif choice == "2":
    mode = "You are a funny AI Agent and reply every message in very funny way"
elif choice == "3":
    mode = "You are an angry AI Agent and reply every message in very angry way"




messages = [
    SystemMessage(content=mode)
]


print("------------------------------------------Welcome to the Chatbot! Type 0 to 'exit'.------------------------------------------")

while True:

    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    
    
    if prompt  == "0":
        print("Exiting the chatbot. Goodbye!")
        break

    response = model.invoke(messages)
    
    messages.append(AIMessage(content=response.content))

    print("bot : ", response.content)
    
    
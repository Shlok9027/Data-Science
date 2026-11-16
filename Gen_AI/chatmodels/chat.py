from dotenv import load_dotenv

load_dotenv()



# from langchain_openai import ChatOpenAI

# model =  ChatOpenAI(model="gpt-5", )


# response = model.invoke("Hello, how are you?")


# ###################################from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model

# # Load API key
# load_dotenv()

# # Initialize Gemini model
# model = init_chat_model(
#     "google_genai:gemini-3.7-flash",
#     temperature=0.7,
#     max_retries=3
# )

# # Send prompt
# response = model.invoke("Why do parrots talk?")

# # Display response
# print(response.content)

# model = init_chat_model("google_genai:gemini-3.7-flash")


# response = model.invoke("Why do parrots talk?")
###########################################################




# from langchain.chat_models import init_chat_model

# model = init_chat_model("groq:openai/gpt-oss-120b")

# response = model.invoke("What is the machine learning?")

# print(response.content)


from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-120b")

response = model.invoke("What is the machine learning?")

print(response.content)
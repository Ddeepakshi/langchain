from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
from dotenv import load_dotenv  

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chat_history=[
    SystemMessage(content="You are a helpful assistant that provides concise answers."),                              
]

while True:
    user_input=input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat.")
        break
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)

print("Chat_history:", chat_history)
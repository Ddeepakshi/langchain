from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
prompt = "Explain the theory of relativity in simple terms."
# NOTE: Calling `invoke` may require Google credentials to be configured in your environment.
# If you don't want to invoke the model now, you can comment out the following two lines.
result = model.invoke(prompt)

print(result)
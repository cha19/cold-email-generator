from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()
apikey= os.getenv('groq_api_key')

llm = ChatGroq(
    temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
    model_name='llama-3.3-70b-versatile',
    groq_api_key=apikey)


response = llm.invoke('teh first person to land on the moon')
print(response.content)
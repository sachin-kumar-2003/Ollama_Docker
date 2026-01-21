from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()

client = Client(
    host='http://localhost:11434'
)

try:
    client.pull('gemma3:4b')
except Exception as e:
    print(f"error pulling the model error = ",e)
    
@app.post("/chat")
def chat(message: str = Body(..., description="Write your chat") ):
    response = client.chat(
    model='gemma3:4b',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
    return response['message']['content']
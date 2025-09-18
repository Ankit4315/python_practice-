from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key= os.environ.get("open_api_key")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "you are a virtual assistant name soma skilled in general task like alexa and google cloud"
        },
        {
            "role":"user",
            "content":"what is coding"
        }
    ]
)

print(completion.choices[0].message.content)


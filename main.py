import os, argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("api_key is none")   

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [
    {"role": "user", "content": args.user_prompt},
]


response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

if response.usage is not None:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
else:
    raise RuntimeError("failed api request. no usage of response.")

print(response.choices[0].message.content)
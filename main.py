import os, argparse, sys

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function


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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

def agent():
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions,
        )

        if response.usage is not None:
            if args.verbose == True:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")
        else:
            raise RuntimeError("failed api request. no usage of response.")

        message = response.choices[0].message
        messages.append(message) #appending message from the model back to the model in the next call.

        # Final answer — no tool calls requested
        if message.content is not None and not message.tool_calls:
                print(f"\n\nFinal response:\n{message.content}")
                return  # exits the function, loop is done
                
        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                if result_message["content"] == "":
                    raise Exception("no content")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message) # appending back the tools results into the message
                
    # Fell through all 20 iterations without a final answer
    print("Error: agent hit max iterations without finishing.")
    sys.exit(1)

agent()
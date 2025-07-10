from openai import OpenAI
import json

# Initialize the client. It will read the API key from the
# OPENAI_API_KEY environment variable.
client = OpenAI()

# Simple addition function to demonstrate a tool

def add_numbers(a: float, b: float) -> float:
    return a + b

# Mapping of function names to actual callables
FUNCTIONS = {
    "add_numbers": add_numbers,
}


def main():
    # Example question for the LLM
    question = "What is 2 plus 3?"
    messages = [
        {"role": "user", "content": question}
    ]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "add_numbers",
                "description": "Return the sum of two numbers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"}
                    },
                    "required": ["a", "b"],
                },
            },
        }
    ]

    # Ask the model; it may decide to call the function
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        result = FUNCTIONS[name](**arguments)
        messages.append(message.model_dump())
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "name": name,
            "content": str(result),
        })
        follow_up = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        print(follow_up.choices[0].message.content)
    else:
        print(message.content)


if __name__ == "__main__":
    main()

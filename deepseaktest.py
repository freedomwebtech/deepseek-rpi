from llama_index.llms.groq import Groq
from llama_index.core.llms import ChatMessage, MessageRole

# Initialize Groq LLM (DeepSeek Model)
llm = Groq(
    model="deepseek-r1-distill-llama-70b",
    api_key=""
)

# Initial system message to set context
messages = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are Jarvis, my personal assistant. Be helpful and professional."),
]

# Chat loop
print("Jarvis is online! Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Jarvis: Goodbye!")
        break

    # Append user message to history
    messages.append(ChatMessage(role=MessageRole.USER, content=user_input))

    # Get response from LLM
    response = llm.chat(messages)

    # Print assistant's response
    print(f"Jarvis: {response}\n")

    # Append assistant response to chat history for context
    messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=response))

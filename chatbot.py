import openai
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint ="", 
  api_key="",  
  api_version=""
)

# Initialize the OpenAI API
# operaise Exception("The 'openai.api_key' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key="YOUR API KEY")'") Initialize the conversation list
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]

# Function to interact with GPT-3
def chat_with_gpt3(prompt, conversation):
    model_engine = "gpt-4"
    
    # Add the new user message to the conversation list
    conversation.append({"role": "user", "content": prompt})
    
    # Generate a message from the model
    response = client.chat.completions.create(
    model=model_engine,
    messages=conversation)
    #print(response)
    message_output = response.choices[0].message.content
    #put = response['choices'][0]['message']['content']
    
    # Add the model's message to the conversation list
    conversation.append({"role": "assistant", "content": message_output})
    
    return message_output

# Main chat loop
if __name__ == "__main__":
    print("Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            bot_response = chat_with_gpt3(user_input, conversation)
            print(f"Chatbot: {bot_response}")

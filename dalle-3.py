import openai
import requests
import time

# Load your API key
api_key_path = 'openaiapikey.txt'  # Path to your API key file
with open(api_key_path, 'r') as file:
    api_key = file.read().strip()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Read prompt text from file
prompt_file_path = 'dalleprompt.txt'  # Path to your prompt file
with open(prompt_file_path, 'r') as file:
    prompt_text = file.read().strip()

# Number of images to download
num_images = 2

# Download images
for i in range(num_images):
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt_text,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        image_response = requests.get(image_url)

        if image_response.status_code == 200:
            # Generate a filename with a timestamp
            timestamp = time.strftime("%Y%m%d%H%M%S")
            filename = f"image_{timestamp}_{i + 1}.png"
            with open(filename, "wb") as file:
                file.write(image_response.content)
            print(f"Image {filename} downloaded successfully.")
        else:
            print(f"Failed to download image {i + 1}")

        time.sleep(5)  # Wait to avoid hitting rate limits

    except Exception as e:
        print(f"An error occurred: {e}")

print("Image download process completed.")

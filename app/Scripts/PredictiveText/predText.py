import openai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Replace `YOUR_API_KEY` with your OpenAI API key
openai.api_key = os.getenv("Openai_Api_Key")

# Define the prompt that you want GPT-3 to predict text for
prompt = "I want"

# Use the OpenAI API to generate text
completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the first predicted text from the API response
message = completions.choices[0].text

# Print the predicted text
print(prompt + message)



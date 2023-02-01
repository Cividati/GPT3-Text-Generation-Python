import os
import openai

# Read the API key from an environment variable
openai.api_key = os.environ.get("API_KEY")

# Cache to store the results of previous function calls
cache = {}

def generate_text(prompt):
    # Check if the prompt is in the cache
    if prompt in cache:
        return cache[prompt]

    # Make a new API call if the prompt is not in the cache
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    
    # Store the result in the cache
    cache[prompt] = message
    
    return message

generated_text = generate_text("What is the meaning of life?")
print(generated_text)

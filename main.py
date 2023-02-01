import os
import openai

# Read the API key from an environment variable
openai.api_key = os.environ.get("API_KEY")

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

generated_text = generate_text("What is the meaning of life?")
print(generated_text)

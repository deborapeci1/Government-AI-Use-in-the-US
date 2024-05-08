##This file is a simple code to be able to ask questions to chat-gpt.

import openai

# Set your API key securely
openai.api_key = 'sk-proj-XXfuVD0krWVcxJBNorltT3BlbkFJXGrYbcxhcjldnmAo79hp'

def generate_response(text):
    prompt = f"Answer this question: {text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
    try:
        # Trying to access the response correctly
        answer = response['choices'][0]['message']['content']
    except TypeError:
        # If the first access attempt fails, try a different access pattern
        try:
            answer = response.choices[0].message.content
        except AttributeError:
            # If both attempts fail, print the raw response to understand its structure
            print("Failed to extract message content. Response object:")
            print(response)
            return "Error in extracting message content."
    print(answer)
    return answer

# Example usage
question = "How good is chatgpt for data analysis?"
answer = generate_response(question)


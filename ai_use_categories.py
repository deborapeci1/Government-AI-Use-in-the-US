import pandas as pd
import openai

# Function to load the API key from a file
def load_api_key():
    with open('api-key.txt', 'r') as file:
        return file.readline().strip()

# Load the API key from the secure file
api_key = load_api_key()

# Set the API key for the OpenAI service
openai.api_key = api_key

def load_text(file_path):
    """Load text data from a file."""
    with open(file_path, 'r') as file:
        return file.read()

def categorize_keywords(file_path):
    df = pd.read_csv(file_path)
    keywords = list(set(df['Unique_Keywords'].dropna().tolist()))
    chunks = []
    current_chunk = []
    current_length = 0

    for keyword in keywords:
        addition = len(keyword.split()) + 3
        if current_length + addition > 5000:
            chunks.append(current_chunk)
            current_chunk = [keyword]
            current_length = addition
        else:
            current_chunk.append(keyword)
            current_length += addition

    if current_chunk:
        chunks.append(current_chunk)

    all_categories = []

    for chunk in chunks:
        all_keywords = ' || '.join(chunk)
        prompt = f"Given the following list of AI use case keywords, please organize them into distinct categories based on their primary focus and application: {all_keywords}"
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}]
        )
        all_categories.append(response.choices[0].message.content)

    return all_categories

def refine_categories(text):
    """Use OpenAI API to refine text into 10 distinct categories."""
    prompt = f"Based on the provided text of AI use case categories, please consolidate these into 10 distinct and broad categories, with up to 5 sub-categories which provide context to the use: {text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt + text}]
    )
    return response.choices[0].message.content

def save_categories(categories, output_file):
    """Save the refined categories to a file."""
    with open(output_file, 'w') as file:
        file.write(categories)
    print(f"Categories have been saved to {output_file}")

def main():
    input_file_1 = 'unique_ai_keywords.csv'
    intermediate_output = 'ai_use_case_categories.txt'
    final_output = 'refined_ai_categories.txt'

    # Process initial keywords into categories
    categories = categorize_keywords(input_file_1)
    save_categories('\n'.join(categories), intermediate_output)

    # Load and refine the categories
    categories_text = load_text(intermediate_output)
    refined_categories = refine_categories(categories_text)
    save_categories(refined_categories, final_output)

if __name__ == "__main__":
    main()

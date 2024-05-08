##This file allows users to analyze projects in chunks as to avoid the 16k token limit that gpt-3.5-turbo-0125 model has. 

# Import the necessary packages 
import pandas as pd
import openai

# Load the dataset from a CSV file into a pandas DataFrame

df = pd.read_csv('2023 Consolidated AI Use Case Inventory (PUBLIC).csv')

# Check if the 'Summary' column exists in the DataFrame to avoid runtime errors

if 'Summary' not in df.columns:
    raise ValueError("Summary column not found in the CSV file")

# Set the API key for the OpenAI service to authenticate API requests

openai.api_key = "sk-proj-XXfuVD0krWVcxJBNorltT3BlbkFJXGrYbcxhcjldnmAo79hp"

def summarize_text(text_list):
    # Construct a prompt for the AI to summarize the text in exactly three words
    n=len(text_list)
    block = "||".join(text_list)
    prompt = f"""The United States stands to benefit significantly from harnessing the opportunities of AI to improve government services. 
    The federal government is leveraging AI to better serve the public across a wide array of use cases, including in healthcare, transportation, the environment, and benefits delivery. 
    The federal government is also establishing strong guardrails to ensure its use of AI keeps people safe and doesn’t violate their rights.
    The federal governments is carrying out {n} AI projects, summarized below and separated by '||'. 
    Please extract up to 10 keywords that best describe how the US government is harnessing AI to improve government operations and services. 
    The summaries are: {block} """
    
    # Make a request to the OpenAI API using the specified model and prompt
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}]
        )
    # Print the API response to console for debugging purposes
    print("Response:", response)   
    
    # Extract the summary from the API response and return it
    return response.choices[0].message.content
        

def batch_summarize_texts(texts, batch_size=10):
    """ 
    Summarizes texts in batches to efficiently use API calls.
    This function divides the text into batches and processes each batch separately to manage API rate limits and response times.
    """
    summaries = [] # List to hold all summaries
    
    # Process each batch of texts
    for i in range(0, len(texts), batch_size):
        # Select a subset of texts according to the current batch index
        batch_texts = texts[i:i+batch_size]
        
        # Apply the summarize_text function to each text in the current batch and collect results
        
        
        batch_summaries = summarize_text(batch_texts) 
        
        # Extend the main list of summaries with the summaries from the current batch
        
        summaries.append(batch_summaries)
        
    print("Summaries Split:", summaries)
    return summaries
# Extract the list of summaries from the DataFrame
texts_to_summarize = df['Summary'].tolist()[:10]

# Process the summaries
generated_summaries = batch_summarize_texts(texts_to_summarize, batch_size=10)

# Create a DataFrame from the generated summaries
summaries_df = pd.DataFrame(generated_summaries, columns=['Generated Summaries'])

# Save the DataFrame to a new CSV file
summaries_df.to_csv('ai_use_grouped_summaries.csv', index=False)

print("Summaries have been saved to 'ai_use_grouped_summaries.csv'")





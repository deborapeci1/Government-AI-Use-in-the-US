# Import the necessary packages 
import pandas as pd
import openai

# Load the dataset from a CSV file into a pandas DataFrame

df = pd.read_csv('2023 Consolidated AI Use Case Inventory (PUBLIC).csv')

# Load the dataset from a CSV file into a pandas DataFrame
df = pd.read_csv('2023 Consolidated AI Use Case Inventory (PUBLIC).csv')

# Display the number of columns and their names
print("Number of columns:", len(df.columns))
print("Column names:", df.columns.tolist())

# Calculate entries per column and count of empty entries
column_info = df.describe(include='all').loc[['count']]
column_info.loc['missing'] = df.shape[0] - column_info.loc['count']

# Display entries per column and how many empty entries
print("Entries and empty entries per column:")
print(column_info.transpose())

# Check if the 'Summary' column exists in the DataFrame to avoid runtime errors

if 'Summary' not in df.columns:
    raise ValueError("Summary column not found in the CSV file")

# Function to load the API key from a file
def load_api_key():
    with open('api-key.txt', 'r') as file:
        return file.readline().strip()

# Load the API key from the secure file
api_key = load_api_key()

# Set the API key for the OpenAI service
openai.api_key = api_key

def summarize_text(text):
    # Construct a prompt for the AI to summarize the text in exactly three words
    prompt = f"""Please read the following description of an AI use case: {text}, 
    and extract up to 10 keywords that specifically identify the type of AI model being used 
    and its primary application or purpose. List the keywords in a concise format, 
    ensuring each term distinctly communicates either the model type or the specific use case. 
    Focus on selecting terms that are clear and descriptive of the AI's functionality and application.""" 
    
    # Make a request to the OpenAI API using the specified model and prompt
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}]
        )
    # Print the API response to console for debugging purposes
    print(response)    
    
    # Extract the summary from the API response and return it
    return response.choices[0].message.content
        
 
def batch_summarize_texts(texts, batch_size=50):
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
        batch_summaries = [summarize_text(text) for text in batch_texts]
        
        # Extend the main list of summaries with the summaries from the current batch
        summaries.extend(batch_summaries)
    return summaries

# Apply the batch summarization function to the 'Summary' column of the DataFrame
df['AI_Keywords'] = batch_summarize_texts(df['Summary'].tolist())

# Save the DataFrame with the new 'AI_Keywords' column to a CSV file, effectively storing the AI-generated summaries
df.to_csv('summarized_ai_use_cases.csv', index=False)

# Print the first few entries of the DataFrame to verify that the summaries have been added correctly
print(df[['Summary', 'AI_Keywords']].head())

# Deduplicating keywords
all_keywords = set()
df['AI_Keywords'].dropna().apply(lambda x: all_keywords.update(x.split(',')))

# Converting the set of keywords to a DataFrame and saving it
unique_keywords_df = pd.DataFrame(list(all_keywords), columns=['Unique_Keywords'])
unique_keywords_df.to_csv('unique_ai_keywords.csv', index=False)
print(f"Unique keywords saved to 'unique_ai_keywords.csv'. Total unique keywords: {len(all_keywords)}")
##This file allows for the users to test chat bot's response at different cutoffs


import pdfplumber
import openai


# Load your API key from an environment variable or secure storage
api_key = "sk-proj-XXfuVD0krWVcxJBNorltT3BlbkFJXGrYbcxhcjldnmAo79hp"  # Ensure your API key is securely stored and not exposed in the code

# Set up the client with your API key
openai.api_key = api_key

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def generate_summary(text, cutoff):
    if len(text) > cutoff:
        text = text[:cutoff]
    prompt = f"Summarize in 5 sentences the following: {text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def experiment_with_cutoffs(pdf_path, cutoffs):
    text = extract_text_from_pdf(pdf_path)
    summaries = {}
    for cutoff in cutoffs:
        summary = generate_summary(text, cutoff)
        summaries[cutoff] = summary
        print(f"\nSummary with cutoff {cutoff} characters:")
        print(summary)
    return summaries

# Define cutoffs to experiment with
cutoffs = [1000, 5000, 10000, 15000]

# Run the experiment on each document
risk_mitigation_summaries = experiment_with_cutoffs("EO-risk-mitigation.pdf", cutoffs)
transparency_summaries = experiment_with_cutoffs("EO-transparency.pdf", cutoffs)
##This file allows for the users to test different prompts at different cutoffs

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

def generate_summary(text, cutoff, prompt_style):
    if len(text) > cutoff:
        text = text[:cutoff]
    prompt = f"{prompt_style} {text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def experiment_with_cutoffs_and_prompts(pdf_path, cutoffs, prompts):
    text = extract_text_from_pdf(pdf_path)
    results = {}
    for cutoff in cutoffs:
        results[cutoff] = {}
        for prompt in prompts:
            summary = generate_summary(text, cutoff, prompt)
            results[cutoff][prompt] = summary
            print(f"\nSummary with cutoff {cutoff} characters and prompt '{prompt}':")
            print(summary)
    return results

# Define cutoffs and prompts to experiment with
cutoffs = [1000, 5000, 10000, 15000]
prompts = [
    "Please summarize the following document in five concise sentences:",
    "Identify and describe the most important points in the following text:",
    "Provide an executive summary for the document below:",
    "You are a professor researching AI and governance in the United States. You have been given the task to read the document below and summarize the key takeaways."
]

# Run the experiment on each document
risk_mitigation_results = experiment_with_cutoffs_and_prompts("EO-risk-mitigation.pdf", cutoffs, prompts)
transparency_results = experiment_with_cutoffs_and_prompts("EO-transparency.pdf", cutoffs, prompts)

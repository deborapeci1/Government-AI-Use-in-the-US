import pdfplumber
import openai

openai.api_key = "sk-proj-XXfuVD0krWVcxJBNorltT3BlbkFJXGrYbcxhcjldnmAo79hp"

# Load your API key from an environment variable or secure storage
api_key = "sk-proj-XXfuVD0krWVcxJBNorltT3BlbkFJXGrYbcxhcjldnmAo79hp"

# Set up the client with your API key
openai.api_key = api_key

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Example usage
risk_mitigation_text = extract_text_from_pdf("EO-risk-mitigation.pdf")
transparency_text = extract_text_from_pdf("EO-transparency.pdf")


def generate_summary(text, cutoff, document_name):
    if len(text) > cutoff:
        text = text[:cutoff]
    prompt = f"""Please analyze the attached: {text}, and provide a comprehensive summary. Your summary should be in paragraphs and include the following key points:
1. The primary objectives and goals of the policy.
2. The main stakeholders affected by the policy and their roles.
3. Any significant changes or updates compared to previous versions or related policies.
4. The methods and strategies proposed to achieve the stated objectives.
5. The expected outcomes and impact of implementing the policy."""
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = [{
            "role":"user", "content":prompt
            }]
       
    )
    print(f"Summary of {document_name} with {cutoff} characters:")
    return response.choices[0].message.content

def experiment_with_cutoffs(pdf_path, cutoffs):
    text = extract_text_from_pdf(pdf_path)
    document_name = pdf_path.split('/')[-1]  # Extracts file name from path
    summaries = {}
    for cutoff in cutoffs:
        summary = generate_summary(text, cutoff, document_name)
        summaries[cutoff] = summary
        print(summary)
    return summaries

# Define cutoffs to experiment with
cutoffs = [1000, 5000, 10000]

# Run the experiment on each document
risk_mitigation_summaries = experiment_with_cutoffs("EO-risk-mitigation.pdf", cutoffs)
transparency_summaries = experiment_with_cutoffs("EO-transparency.pdf", cutoffs)


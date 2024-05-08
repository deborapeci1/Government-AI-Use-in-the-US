# Government Use of AI in the U.S.: An Overview

## Executive Summary

This repository serves as a resource for academics, policy analysts, AI researchers, and government officials who are delving into the implications of AI policies. It offers tools and insights to enhance the understanding of AI governance. We welcome contributions that help refine our scripts, improve accuracy, and expand functionalities, fostering a collaborative environment aimed at advancing the comprehension of AI policy management.

The project focuses on analyzing the AI use case inventory published by the U.S. government, employing intermediate to advanced Python skills and the OpenAI API. Key objectives include:

1. **Summarizing Policy Actions**: Providing detailed summaries of the government's efforts to monitor AI development, mitigate risks, and enhance transparency in AI usage.
2. **Utilizing AI for Analysis**: Leveraging the OpenAI API to generate insightful summaries of key policy documents.
3. **Evaluating Public AI Use Cases**: Analyzing and categorizing the deployment of AI across federal agencies, focusing on the purpose and scope of its use.

## Documents and Data Analyzed

- **Use Case Inventory**: `2023 Consolidated AI Use Case Inventory (PUBLIC).csv`
- **Executive Orders**:
  - **Advancing Governance, Innovation, and Risk Management for Agency Use of AI**: `EO-risk-mitigation.pdf`
  - **Promoting the Use of Trustworthy Artificial Intelligence in the Federal Government**: `EO-transparency.pdf`

## Scripts

- **Policy Analysis** (`policy.py`): Handles the extraction and analysis of textual data from policy PDF documents.
- **AI Use Inventory Processing** (`ai_use_inventory.py`): Processes the AI use case inventory to extract relevant data and prepare it for analysis.
- **AI Use Categorization** (`ai_use_categories.py`): Categorizes AI uses based on keywords extracted from the inventory and refined through further analysis.

This structured approach not only clarifies the government's strategies concerning AI but also underscores our commitment to promoting transparency and accountability in the deployment of AI technologies within public sectors.
## Policy Analysis Overview

The primary goal of this analysis is to delve into the implications of **federal policies and decisions** regarding artificial intelligence (AI) use across various departments. This project utilizes resources from the [ai.gov](https://www.ai.gov) website, which consolidates all pertinent information, including the latest policy updates and expected changes in one centralized location.

The analysis primarily focuses on two critical **Executive Orders**:
1. **"Executive Order Advancing Governance, Innovation, and Risk Management for Agency Use of AI"** (`EO-risk-mitigation.pdf`)
2. **"Executive Order Promoting the Use of Trustworthy Artificial Intelligence in the Federal Government"** (`EO-transparency.pdf`)

Together, these documents, totaling 39 pages, form the foundation of our analysis. They highlight essential areas such as:
- Enhancing AI governance
- Promoting responsible AI usage
- Managing associated risks, particularly those affecting public rights and safety

These orders not only encourage agencies to adopt best practices and engage in continuous monitoring of AI systems but also emphasize the importance of transparency and accountability in decision-making processes. This initiative builds upon the **AI in Government Act of 2020** and other relevant executive orders, aiming to maximize AI's potential while ensuring public safety and privacy.

### Objectives and Expected Outcomes

These policies aim to improve decision-making processes, enhance public service delivery, and foster greater trust in the federal government's use of AI. They mandate the implementation of AI governance measures and adherence to established guidelines. Recent updates underscore the importance of ethical AI practices and the introduction of roles such as **Chief AI Officers (CAIOs)** to effectively manage AI initiatives.

The anticipated outcomes include:
- Improved capacity of agencies to responsibly implement AI
- Enhanced risk management
- Better public service delivery through optimized AI applications

## Practical Application

In practical terms, the [`policy.py`](./policy.py) script facilitates text analysis using AI. This tool allows users to experiment with chatbot outputs using various prompts and cutoff points to navigate the token limitations of the GPT-3.5-turbo model.

# AI Use Case Inventory Overview

The website provides an extensive inventory of AI applications used by various government departments and agencies. This database features 710 entries, with detailed descriptions totaling about 40,000 words. Due to its vast size and non-uniform formatting, the database poses a challenge for navigation, as each entry requires individual analysis. Manual analysis of this magnitude would require several days and multiple people.

To facilitate efficient analysis, we use two scripts:
- **[ai_use_inventory.py](./ai_use_inventory.py)**: Analyzes each project individually.
- **[ai_use_categories.py](./ai_use_categories.py)**: Extracts keywords and categorizes them into ten principal themes reflecting the government's primary AI applications.

## Categories of AI Use Cases Based on Keywords:

1. **Healthcare and Medical Applications**:
   * Disease detection
   * Drug safety monitoring
   * Chronic Disease Management

2. **Environmental Monitoring and Prediction**:
   * Water quality forecasting
   * Groundwater quality prediction
   * Environmental monitoring

3. **Text Analysis and Natural Language Processing**:
   * Text mining
   * Keyword extraction
   * Natural Language Processing (NLP)

4. **Machine Learning and Data Analysis**:
   * Predictive analytics
   * Stochastic modeling techniques
   * Data analytics

5. **Security and Threat Detection**:
   * Cyber threat identification
   * Anomaly detection
   * Fraud detection

6. **Energy and Resource Optimization**:
   * Energy storage
   * Renewable energy forecasting
   * Energy efficiency analysis

7. **Decision Support and Policy Analysis**:
   * Policy analysis
   * Compliance monitoring
   * Decision-making assistance

8. **Industrial Applications and Process Improvement**:
   * Nonlinear Model Predictive Control (NMPC)
   * Optimization
   * Manufacturing prediction

9. **Research and Development**:
   * Particle physics
   * Scientific computing
   * Material science optimization

10. **Document Analysis and Information Processing**:
   * Document processing
   * Text summarization
   * Named Entity Recognition (NER)

These categorization efforts provide valuable insights into the prevalent AI applications within the government, helping to streamline and enhance the understanding of the use case inventory.

## Opportunities and Challenges in Utilizing AI for Big Data Analysis

### Opportunities

The integration of **Artificial Intelligence (AI)** in data and document analysis presents numerous opportunities for enhancing efficiency and depth of insights. AI technologies enable the handling of diverse data formats and the application of varied analytical prompts to achieve specific outcomes. This versatility is invaluable in extracting meaningful information from large datasets, often leading to discoveries that might not be apparent through traditional methods. Moreover, using AI in data analysis demands a high level of creativity in problem-solving, providing a robust platform for developing and honing these critical skills. As practitioners navigate these complex tasks, they gain substantial knowledge and expertise in AI capabilities and limitations, further enriching their professional growth and understanding of the field.

### Challenges

However, the deployment of AI in analyzing extensive datasets is not without its challenges. One significant limitation encountered in this context is the token restriction imposed by models such as **GPT-3.5**. This model's current configuration allows it to process only up to **16,000 tokens** at a time, which roughly equates to analyzing approximately 8,000 to 12,000 words depending on the complexity and formatting of the text. This constraint necessitates the truncation or summarization of materials to fit within the token limit, potentially leading to the loss of critical information. The need to selectively condense data poses the risk of omitting nuanced details that could be crucial for a comprehensive analysis. However, there is a silver lining: this process helps identify and eliminate superfluous information, thereby streamlining the analysis and focusing on the most pertinent data. This enforced brevity can lead to a more focused and efficient analysis process, although it requires careful consideration to ensure that essential content is not discarded inadvertently.

### Balancing Act

The challenge of token limitations underscores a broader issue in AI-driven analysis: the balance between depth and breadth. While AI can manage vast quantities of data far beyond human capacity, its effectiveness is bounded by the constraints of current technology and model parameters. Each project involving AI in big data analytics must therefore be carefully planned with these limitations in mind, ensuring that the scope and methodology are aligned with the technical capacities of the AI tools employed.

In summary, while AI presents remarkable opportunities for advancing data analysis, its effective utilization requires an intricate understanding of both its potential and its boundaries. This necessitates ongoing research and development to continually enhance AI models, making them more adaptable and capable of handling larger datasets without compromising the depth or accuracy of the analysis.



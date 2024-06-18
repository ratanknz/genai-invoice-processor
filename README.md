## Invoice Processing with AWS Bedrock
This project demonstrates how to process PDF invoices stored in an Amazon S3 bucket using AWS Bedrock, a fully managed service for building generative AI applications. The processed invoice data is extracted and stored in a JSON file.

# GenAI-powered invoice processing & review app

This application uses Amazon Bedrock Knowledge Base - Chat with document feature with Claude Sonnet LLM to extract information from pdf invoices and provides a streamlit app which displays the invoices and extracted information side-by-side for easier review. 

## Prerequisites

- Python 3.x
- Required Python packages (can be installed via `requirements.txt`)
- Store invoices (PDF) insdie S3 bucket inside a folder (e.g. invoice).
- AWS CLI installed an configured

## Steps to Run

### Step 1: Process invoices

```bash
python invoices_processor.py --bucket_name='<<replcace this with the name of the s3 bucket>>' --prefix='<<replace with name of the folder>>' 
# e.g. python invoices_processor.py --bucket_name='gen_ai_demo_bucket' --prefix='invoice'
Replace 
1. <your-bucket-name> with the name of your S3 bucket, and 
2. <folder-prefix> with the prefix (folder path) where the invoices are stored.
```
After successful completion of the job, you should see a invoice folder in your local file system with all the s3 invoices. You will also see a processed_invoice_output.json file with all the metadata extracted by Amazon Bedrock Knowledge Base using Claude Sonnet Model.

### Step 2: Review invoice data extracted by Amazon Bedrock
To review the processed invoice data, you can run the Streamlit app with the following command:

```bash
streamlit run review-invoice-data.py
```
The Streamlit app will open in your default web browser, allowing you to view and interact with the processed invoice data.

## Project Structure

1. invoices_processor.py: The main script for processing invoices stored in an S3 bucket.

2. review-invoice-data.py: The Streamlit app for reviewing the processed invoice data.

3. requirements.txt: List of required Python packages.

4. README.md: This file, containing project documentation.
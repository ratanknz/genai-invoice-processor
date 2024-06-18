# GenAI powered invoice processing and review application

This application uses Amazon Bedrock Knowledge Base with Claude Sonnet LLM to extract information from pdf invoices and provides a streamlit app which displays the invoices and extracted information side-by-side for easier review. 

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

```
After successful completion of the job, you should see a invoice folder in your local file system with all the s3 invoices. You will also see a processed_invoice_output.json file with all the metadata extracted by Amazon Bedrock Knowledge Base using Claude Sonnet Model.

### Step 2: Run the Streamlit app to review pdf invoice and corresponding data extracted by Amazon Bedrock

```bash
python review-invoice-data.py
```
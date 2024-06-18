# GenAI-powered invoice processing & review app

This application uses Amazon Bedrock Knowledge Base with Claude Sonnet LLM to extract information from pdf invoices and provides a streamlit app which displays the invoices and extracted information side-by-side for easier review. 

## Prerequisites

- Python 3.x
- Required Python packages (can be installed via `requirements.txt`)
- Store invoices (PDF) insdie S3 bucket inside a folder (e.g. invoice).
- AWS CLI installed an configured

## Steps to Run
```
pip install -r requirements.txt 
```
### Step 1: Process invoices

```bash
python invoices_processor.py --bucket_name='<<replcace this with the name of the s3 bucket>>' --prefix='<<replace with name of the folder>>' 
# e.g. python invoices_processor.py --bucket_name='gen_ai_demo_bucket' --prefix='invoice'

```
After successful completion of the job, you should see a invoice folder in your local file system with all the s3 invoices. You will also see a processed_invoice_output.json file with all the metadata extracted by Amazon Bedrock Knowledge Base using Claude Sonnet Model.

### Step 2: Review invoice data extracted by Amazon Bedrock
Run the streamlit app to review the pdf invoice and data extracted from it

```bash
python -m streamlit run review-invoice-data.py
```
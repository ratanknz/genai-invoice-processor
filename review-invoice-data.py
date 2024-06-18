import json
import boto3
import streamlit as st
import os
from streamlit_pdf_reader import pdf_reader

local_download_folder = "invoice"
invoice_data_file = "processed_invoice_output.json"

with open(invoice_data_file, 'r') as file:
    invoice_data = json.load(file)

if 'counter' not in st.session_state: st.session_state.counter = 0

# Get list of invoices in folder
pathsToInvoices = [os.path.join(local_download_folder,f) for f in os.listdir(local_download_folder)]
# print(pathsToInvoices)

def next(): 
    # st.write('next ' + str(st.session_state.counter))
    if st.session_state.counter < len(pathsToInvoices):
        with invoice:
            st.header("Invoice")
            invoiceFilePath = pathsToInvoices[st.session_state.counter]
            pdf_reader(invoiceFilePath)
        with data:
            st.header("Data")
            # Split the string based on the first occurrence of '{'
            try:
                text_part, json_part = invoice_data[invoiceFilePath].split('{', 1)
                # Add the opening brace back to the JSON part
                json_part = '{' + json_part
                st.json(json_part)
            except Exception as e:
                st.write(invoice_data[invoiceFilePath])
        if st.session_state.counter < len(pathsToInvoices)-1:
            st.session_state.counter += 1        

def prev():
    # st.write('prev' + str(st.session_state.counter))
    # st.write(len(pathsToInvoices))
    if st.session_state.counter < len(pathsToInvoices):
        # st.write('in if.. in prev')
        with invoice:
            st.header("Invoice")
            invoiceFilePath = pathsToInvoices[st.session_state.counter]
            pdf_reader(invoiceFilePath)
        with data:
            st.header("Data")
            # Split the string based on the first occurrence of '{'
            try:
                text_part, json_part = invoice_data[invoiceFilePath].split('{', 1)
                # Add the opening brace back to the JSON part
                json_part = '{' + json_part
                st.json(json_part)
            except Exception as e:
                st.write(invoice_data[invoiceFilePath])
        if st.session_state.counter > 0:
            st.session_state.counter -= 1

cols = st.columns(2)
with cols[1]: st.button("Next ➡️", on_click=next, use_container_width=True)
with cols[0]: st.button("⬅️ Previous", on_click=prev, use_container_width=True)   

invoice, data = st.columns([1,1])

# # Additional fields
# with st.form(key='invoice_form'):
#     issue = st.checkbox("Issue")
#     notes = st.text_area("Notes")
#     submit_button = st.form_submit_button(label='Submit')

#     if submit_button:
#         st.write("Form submitted!")
#         st.write(f"Issue: {issue}")
#         st.write(f"Notes: {notes}")
#         st.write(f"s3 key: {pathsToInvoices[st.session_state.counter]}" )

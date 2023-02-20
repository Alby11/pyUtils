import os
import glob
import pandas as pd
import json
from fpdf import FPDF
from reportlab.pdfgen import canvas
from pretty_html_table import build_table
# html_table = build_table(df_signal, 'grey_dark')
# Set directory path
directory_path = './'

# Set output directory path
output_directory_path = './'

# Get a list of files in the directory
file_list = os.listdir(directory_path)

# Use glob to filter out JSON files
json_files = glob.glob(directory_path + '*.json')

# Loop through the JSON files and convert them to PDF
for file_path in json_files:
    # Open the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)



# Create an instance of the FPDF class
pdf = FPDF()

pdf.add_page()

#    Loop through the keys in the JSON data and add them as section titles to the PDF document:
#    Loop through the values in the JSON data and add them as section content to the PDF document:

for key in data:
    pdf.set_font('Arial', 'B', 16)
    spaces = len(key)
    pdf.cell(0, 10, key + ": " + ('' * spaces) + str(data[key]), ln=1)
    # pdf.set_font('Arial', 'B', 12)
    # pdf.cell(0, 10, ": " + ('' * spaces) + data[key], ln=1)



#    Output the finished PDF document:
pdf.output('output.pdf', 'F')

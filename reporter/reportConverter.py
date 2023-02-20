import os
import glob
import json
from fpdf import FPDF
from reportlab.pdfgen import canvas

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
#     
#     # Create a PDF object
#     pdf = FPDF()
#     
#     # Add a new page
#     pdf.add_page()
#     
#     # Add content to the PDF
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(40, 10, 'JSON to PDF')
#     pdf.ln()
#     pdf.set_font('Arial', '', 12)
#     pdf.multi_cell(0, 10, str(data))
#     
#     # Save the PDF file
#     output_file_name = os.path.basename(file_path).replace('.json', '.pdf')
#     output_file_path = os.path.join(output_directory_path, output_file_name)
#      pdf.output(output_file_path, 'F')



# Load the JSON data from a file
# with open('data.json', 'r') as file:
#     data = json.load(file)

# Create a new PDF document
pdf = canvas.Canvas('output.pdf')

# Add content to the PDF
pdf.drawString(100, 750, "DATA_SPED: " + data['DATA_SPED'])
pdf.drawString(100, 700, "TITOLO: " + data['TITOLO'])

# Save the PDF
pdf.save()

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

# Loop through the JSON files and load them
for file_path in json_files:
    # Open the JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

df = pd.DataFrame(data)

html = (df.style
            .set_table_styles([{'selector': 'th', 'props': [('background', '#3498db'),('color', 'white')]}])
            .set_properties(**{'font-size': '14px', 'font-family': 'Calibri', 'border-collapse': 'collapse', 'border': '2px solid black', 'text-align': 'center'})
            .set_caption('Table Title')
            .set_table_attributes('border="1" class="dataframe table table-hover table-bordered"')
            .to_html()
      )

with open('output.html', 'w') as f:
    f.write(html)

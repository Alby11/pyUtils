import pandas as pd
import json

# Load the JSON file
with open('example.json') as f:
    data = json.load(f)

# Convert the JSON data to a pandas DataFrame
df = pd.json_normalize(data, 'RIGHE', ['DATA_SPED', 'TITOLO', 'PROGR_SPED', 'DESTINATARI'])

def format_table(dataframe):
    """
    Recursively formats a pandas DataFrame with html_table.
    """
    if isinstance(dataframe, pd.DataFrame):
        return dataframe.to_html(classes='table', index=False)
    elif isinstance(dataframe, pd.Series):
        return format_table(pd.DataFrame(dataframe).transpose())
    else:
        return ''

# Format the DataFrame with html_table
html_table = format_table(df)

from jinja2 import Template

# Load the HTML template
with open('report_template.html') as f:
    template_str = f.read()
    template = Template(template_str)

# Render the template with the HTML table
html_report = template.render(table=html_table)

# Save the HTML report to a file
with open('report.html', 'w') as f:
    f.write(html_report)

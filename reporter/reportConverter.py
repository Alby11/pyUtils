import json
import pandas as pd

# Load the JSON file
with open('example.json') as f:
    data = json.load(f)

# Create a DataFrame from the JSON file
df = pd.json_normalize(data, record_path='RIGHE', meta=['DATA_SPED', 'TITOLO', 'PROGR_SPED', 'DESTINATARI'])

# Remove any empty rows
df = df.dropna(how='all')

# Define a recursive function to generate HTML code for each level
def build_html(row):
    html = '<tr>'
    for index, value in row.iteritems():
        if isinstance(value, pd.DataFrame):
            html += build_html(value.iloc[0])
        else:
            html += f'<td>{value}</td>'
    html += '</tr>'
    return html

# Generate HTML code for each row in the DataFrame
html = ''
for index, row in df.iterrows():
    html += build_html(row)

# Generate the final HTML report
final_html = f'''
<html>
    <head>
        <title>{data['TITOLO']}</title>
    </head>
    <body>
        <h1>{data['TITOLO']}</h1>
        <p>Data spedizione: {data['DATA_SPED']}</p>
        <p>Prog. spedizione: {data['PROGR_SPED']}</p>
        <p>Destinatari: {data['DESTINATARI']}</p>
        <table>
            <thead>
                <tr>
                    <th>UDS</th>
                    <th>COD_ARTMGZ</th>
                    <th>COD_CLIENTE</th>
                    <th>NOMINATIVO</th>
                    <th>D_ARTMGZ</th>
                    <th>PROGR_ETIC</th>
                    <th>QTA</th>
                </tr>
            </thead>
            <tbody>
                {html}
            </tbody>
        </table>
    </body>
</html>
'''

# Save the HTML report to a file
with open('report.html', 'w') as f:
    f.write(final_html)

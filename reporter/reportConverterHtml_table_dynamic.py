import os
import pandas as pd
from pretty_html_table import build_table
import pdfkit
import json

# Directory to watch for new files
watch_dir = "./"

# Loop indefinitely
while True:
# Get list of JSON files in the directory
    json_files = [f for f in os.listdir(watch_dir) if f.endswith('.json')]

# Loop over each JSON file
    for json_file in json_files:
# Read JSON file into Pandas dataframe
        # df = pd.read_json(os.path.join(watch_dir, json_file))
# Create dataframe from JSON
        f = open(json_file)
        data = json.load(f)
        df = pd.json_normalize(data, record_path=['RIGHE'], meta=['DATA_SPED', 'TITOLO', 'PROGR_SPED', 'DESTINATARI'])
        f.close()


# Do whatever you want with the dataframe here
# ...

# Delete the JSON file
        # os.remove(os.path.join(watch_dir, json_file))
        
        html_string = build_table(df, 'blue_light')

        with open('table.html', 'w') as f:
            f.write(html_string)

        pdfkit.from_file('table.html', 'table.pdf')

        # os.remove('table.html')

# Rename columns
    df = df.rename(columns={
        'UDS': 'Unità di vendita',
        'COD_ARTMGZ': 'Codice articolo',
        'COD_CLIENTE': 'Codice cliente',
        'NOMINATIVO': 'Nominativo',
        'D_ARTMGZ': 'Descrizione articolo',
        'PROGR_ETIC': 'Progr. etichetta',
        'QTA': 'Quantità',
        'DATA_SPED': 'Data spedizione',
        'TITOLO': 'Titolo',
        'PROGR_SPED': 'Prog. spedizione',
        'DESTINATARI': 'Destinatari'
    })

# Drop rows where all values are empty
    df = df.dropna(how='all')

# Reset index
    df = df.reset_index(drop=True)

# Print formatted dataframe
    print(df.to_string(index=False))

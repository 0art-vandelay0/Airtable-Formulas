from flask import Flask, render_template
from pyairtable import Api
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)


api_key = os.getenv('API_KEY')
base_id = os.getenv('BASE_ID')
# Initialize the API with your API key
api = Api(api_key)

# Access your table
table = api.table(base_id, '🤖 All Functions and Operators')


@app.route('/')
def index():
    # Fetch records from your main table
    records = table.all()

    # Initialize an empty set for distinct values
    formula_data_types = set()

    # Loop through the records and add distinct values to the set
    for record in records:
        data_type = record['fields'].get('Formula Data Type', [])
        if isinstance(data_type, list):
            # If the data type is a list, add each item to the set
            formula_data_types.update(data_type)
        else:
            # If it's not a list, add the item directly to the set
            formula_data_types.add(data_type)

    return render_template('index.html', formula_data_types=formula_data_types)



if __name__ == '__main__':
    app.run(debug=True)

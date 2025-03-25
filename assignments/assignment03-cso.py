import requests

# Replace 'TABLE_CODE' with the actual PxStat table code of the dataset
table_code = 'TABLE_CODE'
api_url = f'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'
# Fetch the dataset from the CSO API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    with open('cso.json', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Dataset successfully retrieved and saved as 'cso.json'.")
else:
    print(f"Failed to retrieve dataset. HTTP Status Code: {response.status_code}")

import requests
import pandas as pd

# Set up the API endpoint URL
url = (
    'https://newsapi.org/v2/everything?'
    'q=tesla&'
    'from=2024-10-01&'
    'sortBy=publishedAt&'
    'apiKey=YOUR_API_KEY'  # Replace with your API key
)

# Make a request to the API
response = requests.get(url)

# Convert the JSON response to a Python dictionary
data = response.json()

# Print the received data
print(data)

# Check the status of the response
if data['status'] == 'ok':
    # Extract articles from the response
    articles = data['articles']

    # Use pd.json_normalize to convert articles to a DataFrame
    df = pd.json_normalize(articles)

    # Save DataFrame to an Excel file
    output_file = 'articles_output.xlsx'
    df.to_excel(output_file, index=False)

    print(f"Data has been saved to {output_file} successfully!")
else:
    # Handle error cases
    print("Failed to retrieve data:", data.get('message', 'No error message provided.'))
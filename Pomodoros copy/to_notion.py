#to_notion.py
import requests
import os
import pandas as pd

def integrate_csv_to_notion(csv_file_path, notion_api_key, notion_database_id):
    # Read the data from the CSV file
    data = pd.read_csv(csv_file_path)

    # Prepare the data for the Notion database
    notion_data = {
        "parent": { "database_id": notion_database_id },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": "Your Page Title"
                        }
                    }
                ]
            },
            # Add more properties as needed based on your Notion database schema
        }
    }

    # Use the Notion API to create a new page in your Notion database
    headers = {
        "Authorization": f"Bearer {notion_api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2021-05-13"
    }
    response = requests.post("https://api.notion.com/v1/pages", json=notion_data, headers=headers)

    # Check the response status
    if response.status_code == 200:
        print("CSV data integrated successfully into Notion.")
    else:
        print("Failed to integrate CSV data into Notion.")
# Usage example
csv_file_path = '/Users/Tohya/Documents/VS_code_outputs/virt/Pomodoros/responses.csv'
notion_api_key = 'secret_AfYGCpZXtb4LunQaL94t0sRwOEhdoQXtZVhRQgqxZxD'
notion_database_id = 'a286b69e7b7144ebac1ab99643822fae'

integrate_csv_to_notion(csv_file_path, notion_api_key, notion_database_id)

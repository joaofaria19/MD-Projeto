import csv
import json

# Input and output file paths
csv_file_path = 'filtered_file.csv'
json_file_path = 'openai/GPT4.json'

max_entries = 30000
# Read CSV and transform data
data = []
with open(csv_file_path, 'r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for i, row in enumerate(csvreader):
        if i >= max_entries:
            break
        entry = {
            "id": str(i),
            "Prompt": row['instruction'],
            "Completion": row['output']
        }
        data.append(entry)

final_data = {"answers": data}

with open(json_file_path, 'w') as jsonfile:
    json.dump(final_data, jsonfile, indent=2, ensure_ascii=False)

print(f"Data has been written to {json_file_path}")

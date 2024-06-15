import json

json_file_paths = [
    '../meta-llama/Meta-Llama-3-8B-Instruct_1.json',
    '../meta-llama/Meta-Llama-3-8B-Instruct_2.json',
    '../meta-llama/Meta-Llama-3-8B-Instruct_3.json'
]
output_json_file_path = '../meta-llama/Meta-Llama-3-8B-Instruct.json'

merged_data = {"answers": []}

for file_path in json_file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data["answers"]:
            merged_data["answers"].append(entry)


merged_data["answers"].sort(key=lambda x: int(x["id"]))

# Write the sorted merged data to a new JSON file
with open(output_json_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, indent=2, ensure_ascii=False)

print(f"Merged data has been written to {output_json_file_path}")

json_file_paths = [
    '../microsoft/Phi-3-mini-4k-instruct_1.json',
    '../microsoft/Phi-3-mini-4k-instruct_2.json',
    '../microsoft/Phi-3-mini-4k-instruct_3.json'
]
output_json_file_path = '../microsoft/Phi-3-mini-4k-instruct.json'

merged_data = {"answers": []}

for file_path in json_file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data["answers"]:
            merged_data["answers"].append(entry)


merged_data["answers"].sort(key=lambda x: int(x["id"]))

# Write the sorted merged data to a new JSON file
with open(output_json_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, indent=2, ensure_ascii=False)

print(f"Merged data has been written to {output_json_file_path}")

json_file_paths = [
    '../mistralai/Mixtral-8x7B-Instruct-v0.1_1.json',
    '../mistralai/Mixtral-8x7B-Instruct-v0.1_2.json',
    '../mistralai/Mixtral-8x7B-Instruct-v0.1_3.json'
]
output_json_file_path = '../mistralai/Mixtral-8x7B-Instruct-v0.1.json'

merged_data = {"answers": []}

for file_path in json_file_paths:
    with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data["answers"]:
            merged_data["answers"].append(entry)


merged_data["answers"].sort(key=lambda x: int(x["id"]))

# Write the sorted merged data to a new JSON file
with open(output_json_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, indent=2, ensure_ascii=False)

print(f"Merged data has been written to {output_json_file_path}")
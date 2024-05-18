import json
questions = {}
file_path = 'openai/GPT4.json'
with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data["answers"]:
            questions[entry["id"]] = entry["Prompt"]

question_file_path = 'questions/questions.json'         
with open(question_file_path, 'w') as jsonfile:
    json.dump(questions, jsonfile, indent=2, ensure_ascii=False)
        
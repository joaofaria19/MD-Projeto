from flask import Flask, render_template, request, jsonify
from transformers import (
    pipeline, 
    BertForSequenceClassification, 
    BertTokenizerFast,
)

model_path = 'admetaq/bert-base-uncased-llm-classificator'

model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer= BertTokenizerFast.from_pretrained(model_path)
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

app = Flask(__name__)

def llm_classification(text):
    label_mapping = {'Meta-Llama-3-8B-Instruct': 'Meta-Llama-3', 'Phi-3-mini-4k-instruct': 'Phi-3', 'Mixtral-8x7B-Instruct-v0.1': 'Mixtral','GPT4': 'GPT4'}
    res = pipe(text)
    res[0]['label'] = label_mapping[res[0]['label']]
    return res
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/llm', methods=['POST'])
def api_llm():
    data = request.get_json()
    text = data.get('input')

    if len(text) < 50:
        response = "Your text is not valid. It has less than 50 characters."
    elif len(text) > 512:
        response = "Your text is not valid. It has more than 512 characters."
    else: 
        res_obj = llm_classification(text)
        if res_obj[0]['score']<= 0.3:
            response = "The origin of this text is not clear."
        else:     
            response = "The LLM who wrote this text was " + res_obj[0]['label'] + " with a probability of " + str(int(res_obj[0]['score'] * 100)) + "%."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
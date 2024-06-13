from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/llm', methods=['POST'])
def api_llm():
    data = request.get_json()
    text = data.get('input')

    # Call your LLM function here and pass the text as an argument
    # response = llm_function(text)

    # For demonstration, we'll use a placeholder response
    response = "This is the response from the LLM " + text

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
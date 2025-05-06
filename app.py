import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json.get('user_input')
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"根据以下需求推荐学习资源：{user_input}",
        max_tokens=150
    )
    return jsonify({"recommendation": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
添加了 app.py 后端代码
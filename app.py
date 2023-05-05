from flask import Flask, request
from dotenv import load_dotenv
import requests
import json
import os
app = Flask(__name__)

load_dotenv()

@app.route('/',methods = ['GET','POST'])

def webhook():
    try:
        question = request.args.get('question')
        url = 'https://api.openai.com/v1/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
        }
        data = {
        'model': 'text-davinci-003',
        'prompt': question,
        'temperature': 0.9,
        'max_tokens': 1500,
        'top_p': 1,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.6,
        'stop': [" Human:", " AI:"]
    }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = response.json()
        reply = response_data['choices'][0]['text']
    except Exception as e:
        print(e)
    return reply

if __name__ == '__main__':
    app.run(debug=True)
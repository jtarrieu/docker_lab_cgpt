from flask import Flask,request
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_KEY')


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/chatgpt')
def chatgpt():
    args = request.args
    message =args.get("message")
    print(message)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

@app.route('/ask_for_code')
def ask_for_code():
    # retrieving the agrs
    args = request.args
    print(f"args : {args}")
    
    # gets the content
    ask =args.get("ask")
    print(f"content : {ask}")
    
    # gets the language
    language =args.get("language")
    print(f"language : {language}")
    
    # combine them to have create the message
    message = f"""Can you write a code in {language} that
    does this : {ask}
    """
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return completion['choices'][0]['message']['content']

"""
flask --app app run
curl localhost:5000/ask_for_code?language=...&ask=...
http://localhost:5000/ask_for_code?language=python&ask=i%20want%20to%20encode%20a%20string%20in%20base64
"""
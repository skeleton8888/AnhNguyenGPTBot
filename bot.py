import openai
import requests

# Telegram Bot API Key
TELEGRAM_BOT_API_KEY = "6038902773:AAHzQu_lgFtf2h89GDutWLV2hK7cLg7ylFI"

# OpenAI API Key
OPENAI_API_KEY = "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"


openai.api_key = OPENAI_API_KEY

def generate_response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Your text here: ' + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"]
    return message

def handle_request(request):
    text = request.json['message']
    response = generate_response(text)
    return response
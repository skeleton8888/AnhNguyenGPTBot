import requests
import os

# Telegram Bot API Key
TELEGRAM_BOT_API_KEY = "6038902773:AAHzQu_lgFtf2h89GDutWLV2hK7cLg7ylFI"

# OpenAI API Key
OPENAI_API_KEY = "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"

def send_message(chat_id, text):
    """Sends a message to a Telegram chat"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

def get_response_from_openai(prompt):
    """Gets a response from OpenAI API"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 2048,
        "temperature": 0.5
    }
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=data)
    response_text = response.json()["choices"][0]["text"]
    return response_text

def handle_update(update):
    """Handles an incoming Telegram update"""
    message = update["message"]
    chat_id = message["chat"]["id"]
    text = message["text"]
    response_text = get_response_from_openai(text)
    send_message(chat_id, response_text)

def get_updates():
    """Gets updates from Telegram API"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/getUpdates"
    response = requests.get(url)
    return response.json()["result"]

if __name__ == "__main__":
    while True:
        updates = get_updates()
        for update in updates:
            handle_update(update)

def set_webhook(url, bot_token):
    requests.post(f'https://api.telegram.org/bot{bot_token}/setWebhook', data={'url': url})






#webhook
def handle_update(update, bot_token):
    # Extract the message from the update
    message = update['message']['text']
    
    # Process the message and generate a response
    response = "You said: " + message
    
    # Send the response back to the user
    chat_id = update['message']['chat']['id']
    requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage', data={'chat_id': chat_id, 'text': response})

# Set the webhook with the URL of your deployed code
set_webhook("https://startling-brigadeiros-7e4df4.netlify.app", TELEGRAM_BOT_API_KEY)

# Handle incoming updates
update = ... # receive incoming updates from the Telegram API
handle_update(update, TELEGRAM_BOT_API_KEY)
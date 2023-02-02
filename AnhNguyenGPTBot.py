import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

def response(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    token = "6038902773:AAHzQu_lgFtf2h89GDutWLV2hK7cLg7ylFI"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, response))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
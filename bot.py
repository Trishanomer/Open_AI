import os
from pymongo import MongoClient
from pyrogram import Client, filters

# Set up MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['chatbot']
collection = db['chats']

# Set up Pyrogram client
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

app = Client(':memory:', api_id=api_id, api_hash=api_hash, bot_token=bot_token)


def save_chat(chat_id, message):
    collection.insert_one({'chat_id': chat_id, 'message': message})


def get_last_reply(chat_id):
    cursor = collection.find({'chat_id': chat_id}).sort('_id', -1).limit(1)
    if cursor.count() > 0:
        return cursor[0]['message']
    return None


@app.on_message(filters.text)
def handle_message(client, message):
    chat_id = message.chat.id
    user_input = message.text

    # Save the current chat message
    save_chat(chat_id, user_input)

    # Get the last reply from the database
    last_reply = get_last_reply(chat_id)

    if last_reply:
        # Reply based on the last user's message
        bot_reply = last_reply
    else:
        # If there is no previous reply, use a default response
        bot_reply = "Hello, how can I assist you?"

    # Save the bot's reply
    save_chat(chat_id, bot_reply)

    # Send the bot's reply to the user
    message.reply_text(bot_reply)


if __name__ == '__main__':
    app.run()

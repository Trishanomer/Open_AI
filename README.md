# Telegram ChatBot with Pyrogram and MongoDB

This is a Telegram chatbot built using Pyrogram, an elegant Python library for the Telegram Bot API, and MongoDB, a popular NoSQL database. The bot can store chat history and reply to messages based on the ongoing chat conversation.

## Features

- Store chat history in a MongoDB database
- Analyze ongoing chat conversation to generate replies
- Reply to messages based on previous chat interactions
- Support for multiple chat languages
- Easy deployment on various platforms

## Prerequisites

- Python 3.6 or higher
- MongoDB database
- Pyrogram library
- pymongo library

## Installation

1. Clone this repository:git clone https://github.com/your_username/telegram-chatbot.git

2. Install the required dependencies:pip install -r requirements.txt


3. Set up your MongoDB database and update the database connection details in the `bot.py` file.

4. Obtain the API credentials for your Telegram bot and update the `.env` file with the required information:

API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token


5. Start the bot: python bot.py



## Usage

- Once the bot is running, add it to your Telegram group or start a private chat with it.

- The bot will store the chat history and analyze the ongoing conversation to generate replies.

- Interact with the bot and observe how it responds based on previous chat interactions.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).






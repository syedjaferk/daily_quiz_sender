import json
import argparse
from sender import Sender
from datetime import datetime

parser = argparse.ArgumentParser(description="Quiz")

parser.add_argument('--category', type=str, help='Category', required=True)
parser.add_argument('--telegram_url', type=str, help='Telegram Bot Url With Token', required=True)
parser.add_argument('--chat_id', type=str, help='Chat ID', required=True)

args = parser.parse_args()

category = args.category
DEST_PATH = f"questions/{category}/"

# Construct File Name
current_date = datetime.today().strftime('%Y_%m_%d')
file_name = f"{DEST_PATH}quiz_{current_date}.json"


# Read Question
with open(file_name, 'r') as file:
    data = json.load(file)

data.update({
    "chat_id": args.chat_id,
    "type": "quiz",
    "is_anonymous": False
})

# Send Poll
sender = Sender(question=data, telegram_bot_url=args.telegram_url)
sender.run()


import json
import argparse
from sender import Sender
from datetime import datetime

parser = argparse.ArgumentParser(description="Quiz")

parser.add_argument('--category', type=str, help='Category', required=True)
parser.add_argument('--telegram_url', type=str, help='Telegram Bot Url With Token', required=True)
parser.add_argument('--chat_id', type=str, help='Chat ID', required=True)
parser.add_argument('--message_thread_id', type=str, help="Message Thread ID", required=True)

args = parser.parse_args()

category = args.category
DEST_PATH = f"message/{category}/"

# Construct File Name
current_date = datetime.today().strftime('%Y-%m-%d')
file_name = f"{DEST_PATH}1d1c_{current_date}.json"


# Read Question
with open(file_name, 'r') as file:
    data = json.load(file)

message = f"""
✨ Command of the Day: {data["title"]} 

🛑 {data["english_description"]}  

🌍 {data["tamil_description"]} 

🖥️ Example:  
```
{data["example"]}
```
"""

message_val = {
    "chat_id": args.chat_id,
    "text": message,
    "parse_mode": "Markdown",
    "message_thread_id": args.message_thread_id
}

print(message_val)

# Send Poll
sender = Sender(question=message_val, telegram_bot_url=args.telegram_url)
sender.run()

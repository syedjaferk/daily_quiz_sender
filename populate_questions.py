import json
from datetime import datetime, timedelta

START_DATE = "2025-03-02"
date_format = "%Y-%m-%d"
category = "1d1c"
DEST_PATH = f"questions/{category}/"
ALL_QUESTIONS = f"questions/{category}/{category}_all_questions.json"

questions_file = open(ALL_QUESTIONS, "r")
questions = json.load(questions_file)
questions_file.close()
for itr, question in enumerate(questions["questions"]):
    date_object = datetime.strptime(START_DATE, date_format)
    date_object_with_delta = date_object + timedelta(days=itr)
    date_object_str = date_object_with_delta.strftime('%Y_%m_%d')
    destination_file = f"quiz_{date_object_str}.json"
    quiz_file = open(DEST_PATH + destination_file, "w")
    json.dump(question, quiz_file)
    quiz_file.close()

import datetime
import re


def get_date(input_str):
    days_regex = re.compile(r"(\d+) days")
    today_regex = re.compile(r"today")
    tomorrow_regex = re.compile(r"tomorrow")
    yesterday_regex = re.compile(r"yesterday")
    
    days_match = days_regex.search(input_str)
    today_match = today_regex.search(input_str)
    tomorrow_match = tomorrow_regex.search(input_str)
    yesterday_match = yesterday_regex.search(input_str)
    if days_match:
        days = int(days_match.group(1))
        if "ago" in input_str:
            days *= -1
        target_date = datetime.date.today() + datetime.timedelta(days=days)
    elif today_match:
        target_date = datetime.date.today()
    elif tomorrow_match:
        target_date = datetime.date.today() + datetime.timedelta(days=1)
    elif yesterday_match:
        target_date = datetime.date.today() - datetime.timedelta(days=1)
    else:
        return "I'm sorry, I didn't understand your question."
    return target_date.strftime("%B %d, %Y")

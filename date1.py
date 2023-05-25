import datetime
import re


def get_date(input_str):
    # Define regex patterns to match various date-related questions
    days_regex = re.compile(r"(\d+) days")
    today_regex = re.compile(r"today")
    tomorrow_regex = re.compile(r"tomorrow")
    yesterday_regex = re.compile(r"yesterday")

    # Parse the input string for relevant date information
    days_match = days_regex.search(input_str)
    today_match = today_regex.search(input_str)
    tomorrow_match = tomorrow_regex.search(input_str)
    yesterday_match = yesterday_regex.search(input_str)

    # Calculate the target date based on the parsed input
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

    # Format the target date as a string and return it
    return target_date.strftime("%B %d, %Y")

# # Example usage
# input_str = "what's the date 5 days ago?"
# print(get_date(input_str))

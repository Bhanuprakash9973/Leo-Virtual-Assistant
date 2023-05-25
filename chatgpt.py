# openai integration

import openai

apiKey = "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"

openai.api_key = apiKey

messages = [
    {
        'role': 'system',
        'content': 'you are context extractor for my commands.'
    },
]


def askgpt(ip):
    while True:
        message = ip
        if message:
            messages.append(
                {'role': 'user', 'content': message},
            )
            chat = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=messages,
            )
        reply = chat.choices[0].message.content
        # print(f"ChatGPT: {reply}")
        messages.append({'role': 'assistant', 'content': reply})
        return reply

# while True:
#     message = input("User: ")
#     if message:
#         messages.append(
#             {'role': 'user', 'content': message},
#         )
#         chat = openai.ChatCompletion.create(
#             model='gpt-3.5-turbo',
#             messages=messages,
#         )
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({'role': 'assistant', 'content': reply})

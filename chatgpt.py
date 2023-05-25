import openai

apiKey = "{YOUR API KEY}"

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
        messages.append({'role': 'assistant', 'content': reply})
        return reply

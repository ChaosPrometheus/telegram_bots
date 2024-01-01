from pyrogram import Client, filters
import openai

api_id = 
api_hash = ''
token = ""
openai.api_key = ""

app = Client("my_bot", api_id, api_hash, bot_token=token)

@app.on_message(filters.text)
def handle_message(client, message):
    user_message = message.text
    ai_response = chat_with_gpt(user_message)
    app.send_message(chat_id=message.chat.id, text=ai_response)

def chat_with_gpt(user_input):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
        )
    print(user_input)
    ai_response = response.choices[0].text.strip()
    return ai_response
    

app.run()

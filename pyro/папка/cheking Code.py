from pyrogram import Client, filters
api_id = 22339175
api_hash = '17f2077161c4b1fa273b22569b945dd8'
app = Client("kroka", api_id, api_hash)

@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)

app.run()
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep

api_id = 
api_hash = ""

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" 
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.01) 
			tbp = tbp + text[0]
			text = text[1:]
			msg.edit(tbp)
			sleep(0.01)

		except FloodWait as e:
			sleep(e.x)

app.run()
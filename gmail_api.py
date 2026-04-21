from dotenv import load_dotenv
import os

load_dotenv()

creds_file = os.getenv("CREDENTIALS_FILE")
token_file = os.getenv("TOKEN_FILE")


import ezgmail
with open("trending.html","r",encoding="utf-8")as f:
    html_content=f.read()
emails=["malay88patra@gmail.com","vivekbanerjee64@gmail.com"]
for email in emails:
    ezgmail.send(email,"Top Trending Repos",html_content,mimeSubtype='html')
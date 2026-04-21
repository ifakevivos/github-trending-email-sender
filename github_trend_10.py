import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://github.com"
url = "https://github.com/trending"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

h2 = soup.select("article.Box-row>h2")
p = soup.select("article.Box-row>p")
link = soup.select("article.Box-row>h2>a[href]")

with open("trending.html", "w", encoding="utf-8") as f:

    f.write("""
    <html>
    <body style="font-family: Arial, sans-serif; line-height:1.6; max-width:700px; margin:auto;">

    <h2 style="text-align:center; color:#333;">Top 10 Trending GitHub Repositories</h2>

    <div style="margin-top:20px;">
    """)

    for i in range(10):
        title = " ".join(h2[i].text.split())
        desc = " ".join(p[i].text.split())
        repo_url = urljoin(base_url, link[i].get("href"))

        f.write(f"""
        <div style="margin-bottom:20px;">
            <p style="margin:0;"><b>{i+1}. {title}</b></p>
            <p style="margin:5px 0 0 15px; color:#555;">
                {desc}
            </p>
            <p style="margin:5px 0 0 15px;">
                <a href="{repo_url}" style="color:#0366d6; text-decoration:none;">
                    View Repository
                </a>
            </p>
        </div>
        """)

    f.write(f"""
    </div>

    <p style="margin-top:30px; text-align:center; color:#666; font-size:14px;">
        More trending repositories: <br>
        <a href="{url}" style="color:#0366d6;">{url}</a>
    </p>

    <p style="text-align:center; margin-top:20px; font-size:13px; color:#888;">
        <b>THANK YOU</b><br>
        Idea Credit: Malay Patra
    </p>

    </body>
    </html>
    """)
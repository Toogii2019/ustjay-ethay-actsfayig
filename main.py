import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


@app.route('/')
def home():
    query_args = {'input_text': get_fact()}
    res = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', query_args)
    redirected_link = "#"
    for i in res.history:
        if i.status_code == 302:
            redirected_link = i.headers.get('Location')
    return "<h1><img src='static/Wizard.jpg' width='600' height='400'></h1> \r\n <a href='{0}'>Click here to see magic - {0}</a>".format(redirected_link)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)


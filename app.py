from flask import *
from gtts import *
import os

if os.path.isfile('./static/output.mp3'):
    os.remove('./static/output.mp3')
else:
    pass

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']

        output = gTTS(text=text, lang=lang, slow=False)
        output.save('./static/output.mp3')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from nlp.summarizer import summarize

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def get_summary():
    review = request.form["review"]
    summary = summarize(review)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)

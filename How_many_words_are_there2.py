from flask import Flask, render_template, request

app = Flask(__name__)

def word_count(words):
    number_words = len(words.split())
    if number_words < 0:
        return "Less than Zero"
    if number_words == 0:
        return "Zero"
    if number_words == 1:
        return "One"
    if number_words == 2:
        return "Two"
    if number_words == 3:
        return "Three"
    if number_words == 4:
        return "Four"
    if number_words == 5:
        return "Five"
    if number_words == 6:
        return "Six"
    if number_words == 7:
        return "Seven"
    if number_words == 8:
        return "Eight"
    if number_words == 9:
        return "Nine"
    if number_words == 10:
        return "Ten"
    if number_words > 10:
        return "More than ten"
    return None

@app.route("/",methods=["GET","POST"])
def home():
    result = None
    if request.method == "POST":
        phrase = request.form["phrase"]
        result = word_count(phrase)
    return render_template("How_many_words_are_there.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)

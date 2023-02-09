from flask import Flask,request,render_template
from textblob import TextBlob




app = Flask(__name__)

@app.route("/")
def home():
    result = ""
    return render_template('index.html',result=result)

@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        result = request.form['text']

        blob = TextBlob(result)
        for sentence in blob.sentences:
            result = sentence.sentiment.polarity

        if result > 0:
            return render_template('index.html',message="The review is Positive😊")

        elif result == 0:
            return render_template('index.html', message="The review is Neutral😐")
        else:
            return render_template('index.html', message="The review is Negative☹️")

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)





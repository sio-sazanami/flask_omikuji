from flask import Flask, request, render_template
import random

app = Flask(__name__)

omikuji = ["ウルトラ大吉","大吉","中吉","小吉","吉","末吉","ウルトラ凶","あけおめ!今年もよろしく!"]
prob    = [0.02, 0.089, 0.15, 0.18, 0.25, 0.3, 0.01, 0.001]

@app.route("/",methods=["POST","GET"])
def uranai():
    if request.method == "POST":
        if request.form['send'] == "1回占う":
            return render_template('index.html',result=random.choices(omikuji, weights=prob)[0])
        if request.form['send'] == "10回占う":
            return render_template('index.html',result=random.choices(omikuji, weights=prob, k=10))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
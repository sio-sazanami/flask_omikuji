from flask import Flask, request, render_template
import random
app = Flask(__name__)

omikuji = ["ウルトラ吉","大吉","中吉","吉","小吉","ウルトラ凶"]
prob    = [0.02, 0.07, 0.2, 0.3, 0.4, 0.01]
html1="""
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>あけおめ2022おみくじ</title>
<h1>おみくじサイト</h1>
今年の運勢はこれで決まり！<br>
10連ガチャもありますヨ<br><br>
<form action='/' method='POST'>
    <input type='submit' name="send" value='1回占う'/>
    <input type='submit' name="send" value='10回占う'/>
</form>
<table border="1">
        <caption>おみくじ排出確率表</caption>
        <tr>
            <th>種類</th>
            <td>排出確率</td>
        </tr>
        <tr>
            <th>ウルトラ吉</th>
            <td>2%</td>
        </tr>
        <tr>
            <th>大吉</th>
            <td>7%</td>
        </tr>
        <tr>
            <th>中吉</th>
            <td>20%</td>
        </tr>
        <tr>
            <th>吉</th>
            <td>30%</td>
        </tr>
        <tr>
            <th>小吉</th>
            <td>40%</td>
        </tr>
        <tr>
            <th>ウルトラ凶</th>
            <td>1%</td>
        </tr>
    </table>
"""

@app.route("/",methods=["POST","GET"])
def hello():
    if request.method == "POST":
        if request.form['send'] == "1回占う":
            return render_template('index.html',result=random.choices(omikuji, weights=prob)[0])
        if request.form['send'] == "10回占う":
            return render_template('index.html',result=random.choices(omikuji, weights=prob, k=10))
    return html1

if __name__ == "__main__":
    app.run()
from flask import Flask, request, render_template
import random
app = Flask(__name__)

omikuji = ["ウルトラ大吉","大吉","中吉","小吉","吉","末吉","ウルトラ凶","あけおめ！今年もよろしく!"]
prob    = [0.02, 0.089, 0.15, 0.18, 0.25, 0.3, 0.01, 0.001]
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
            <td>レアリティ</td>
            <td>排出確率</td>
        </tr>
        <tr>
            <th>ウルトラ大吉</th>
            <td>SSR</td>
            <td>2%</td>
        </tr>
        <tr>
            <th>大吉</th>
            <td>SR</td>
            <td>8.9%</td>
        </tr>
        <tr>
            <th>中吉</th>
            <td>R</td>
            <td>15%</td>
        </tr>
        <tr>
            <th>小吉</th>
            <td>R</td>
            <td>18%</td>
        </tr>
        <tr>
            <th>吉</th>
            <td>N</td>
            <td>25%</td>
        </tr>
        <tr>
            <th>末吉</th>
            <td>N</td>
            <td>30%</td>
        </tr>
        <tr>
            <th>ウルトラ凶</th>
            <td>逆にSSR</td>
            <td>1%</td>
        </tr>
        <tr>
            <th>シークレット</th>
            <td>UR</td>
            <td>0.1%</td>
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
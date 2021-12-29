from flask import Flask, request, render_template
import random

app = Flask(__name__)

omikuji = ["ウルトラ大吉","大吉","中吉","小吉","吉","末吉","ウルトラ凶","あけおめ!今年もよろしく!"]
prob    = [0.03, 0.09, 0.15, 0.18, 0.20, 0.20, 0.03, 0.01]
rarity_dic = {"ウルトラ大吉": "SSR",
              "大吉": "SR",
              "中吉": "R",
              "小吉": "R",
              "吉": "N",
              "末吉": "N",
              "ウルトラ凶": "逆にSSR?",
              "あけおめ!今年もよろしく!": "UR"
              }

def rarity(results):
    disp_li = [[0 for j in range(2)] for i in range(len(results))] #[くじ種，レア度]で格納するリスト
    i=0
    for result in results:
        disp_li[i][0] = result
        disp_li[i][1] = rarity_dic[result]
        i+=1
    return disp_li

@app.route("/",methods=["POST","GET"])
def uranai():
    if request.method == "POST":
        if request.form['send'] == "1回占う":
            return render_template('index.html',results=rarity(random.choices(omikuji, weights=prob)))
        if request.form['send'] == "10回占う":
            return render_template('index.html',results=rarity(random.choices(omikuji, weights=prob, k=10)))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
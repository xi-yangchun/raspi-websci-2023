from flask import Flask, render_template,request #追加
import json
import datetime
from threading import Thread
import urllib
import alarm

app = Flask(__name__)
global AC
AC=alarm.alarmclock()
"""
* 未実装のもの
 - クエリパラメータから受け取った時刻をACのtarg_hour,minに代入

"""
@app.route('/',methods=["GET","POST"])
def index():
    if request.method=="GET":
        if "lightOut" in request.args.keys():
            lo=int(request.args["lightOut"])
            AC.set_lo(lo)
            print(lo)
        if "th" in request.args.keys():
            th=int(request.args["th"])
            AC.set_th(th)
            print(th)
        if "alarm" in request.args.keys():
            altime=(request.args["alarm"])
            #deal alarm time by splitting, for example
            alis=altime.split(":")
            AC.set_targ_time(int(alis[0]),int(alis[1]))
            print(altime)
    return render_template('index.html')

def keep_alive():
    t = Thread(target=run)
    t1=Thread(target=AC.run)
    t2=Thread(target=AC.hold_beep)
    t.start()
    t1.start()
    t2.start()

## おまじない
def run():
    app.run(debug=False, host="192.168.1.70")
keep_alive()
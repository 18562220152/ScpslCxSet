import requests
import time
import re
import json
import time
from flask import Flask, jsonify,request
import random
app = Flask(__name__)
se = requests.session()
@app.route('/', methods=['GET'])
def home():
    if __name__ == '__main__':
        ip = mode = request.args.get("ip",default="")
        if (ip == ""):
            return("IP不得为空")
        else:
            Post_url = "http://go.nspnet.top:200/page/api/scpserversinfo.aspx?ip="+ip  # 自己想办法弄到key
            Text = se.post(Post_url).text.replace("'", '"').replace('/ ', '/')
            ra = json.loads(Text)
            print(ra)
            json_str = json.dumps(ra)
            data1 = json.loads(json_str)
            T = data1['Players']
            IP = data1['IP']
            Time = data1['time']
            n = "\n"
        return("服务器IP"+IP+n+'在线人数:'+T+n+"时间:"+Time)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5474)

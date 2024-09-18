from flask import Flask, render_template, request, jsonify
import requests
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11275',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'xweb_xhr': '1',
    'Referer': 'https://tingke.xmu.edu.cn/app/index',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


@app.route('/get_all_class', methods=['POST'])
def get_all_class():
    try:
        data = request.get_json()
        r = requests.post('https://tingke.xmu.edu.cn/app/viewXsKqDetail', headers=headers, data=data)
        json = r.json()
        json = json['Rows']['kc']
        return_data = {}
        return_data['data'] = []
        for item in json:
            _tmp = {
                'qdCode': item['qdCode'],
                'jsXm': item['jsXm'],
                'kcMc': item['kcMc'],
                'kkXy': item['kkXy'],
                'skDd': item['skDd']
            }
            return_data['data'].append(_tmp)
        return_data['status'] = 1
        return return_data
    except Exception as e:
        return_data = {}
        return_data['status'] = 0
        print(e)
        return return_data

@app.route('/get_qiandao_detail', methods=['POST'])
def get_class_detail():
    try:
        data = request.get_json()
        r = requests.post('https://tingke.xmu.edu.cn/app/getQdXsList', headers=headers, data=data)
        json = r.json()
        json = json['Rows']
        return_data = {}
        return_data['data'] = []
        for item in json:
            # if item['xsXh'] != data['userCode']:
            #     continue
            _itmp = {
                "xsQdQkMc": item['xsQdQkMc'],
                "skXsStr": item['skXsStr'],
                "uid": item['uid'],
                "xsXm": item['xsXm'],
                "xsXh": item['xsXh']
            }
            return_data['data'].append(_itmp)
        return_data['status'] = 1
        return return_data
    except Exception as e:
        return_data = {}
        return_data['status'] = 0
        print(e)
        return return_data


@app.route('/update_qiandao_info', methods=['POST'])
def update_qiandao():
    try:
        data = request.get_json()
        # if data['xsXh'] != data['userCode']:
        #     return_data = {}
        #     return_data['status'] = 0
        #     return_data['msg'] = '大坏蛋，你不是这个人'
        #     return return_data
        r = requests.post('https://tingke.xmu.edu.cn/app/updateQdInfo', headers=headers, data=data)
        if r.ok:
            return_data = {}
            return_data['status'] = 1
            return_data['msg'] = "修改成功"
            return return_data
        else:
            return_data = {}
            return_data['status'] = 0
            return_data['msg'] = "修改失败"
            return return_data
    except Exception as e:
        return_data = {}
        return_data['status'] = 0
        return_data['msg'] = "修改失败"
        return return_data
    

@app.route('/update_qiandao_present', methods=['POST'])
def update_qiandao_present():
    """
    更新签到状态 \n
    :param: sign, userCode, unitCode, skXs(1是线下), uid, xsXh 
    """
    try:
        data = request.get_json()
        # if data['xsXh'] != data['userCode']:
        #     return_data = {}
        #     return_data['status'] = 0
        #     return_data['msg'] = '大坏蛋，你不是这个人'
        #     return return_data
        r = requests.post('https://tingke.xmu.edu.cn/app/updateSkXsInfo', headers=headers, data=data)
        if r.ok:
            return_data = {}
            return_data['status'] = 1
            return_data['msg'] = "修改成功"
            return return_data
        else:
            return_data = {}
            return_data['status'] = 0
            return_data['msg'] = "修改失败"
            return return_data
    except Exception as e:
        return_data = {}
        return_data['status'] = 0
        return_data['msg'] = "修改失败"
        return return_data


if __name__ == '__main__':
    app.run(debug=True)
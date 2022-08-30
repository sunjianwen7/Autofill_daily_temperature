# coding=utf-8
import datetime
import json
import requests
#sjw
def renzheng(name,password):
    url = "http://dcmx.tjdz.net/auth/oauth/token?randomStr=undefined&grant_type=password&scope=server"
    payload='username='+str(name)+'&password='+str(password)
    headers = {
    'Host': 'dcmx.tjdz.net',
    'Accept': '*/*',
    'TENANT-ID': '1',
    'Authorization': 'Basic YXBwOmFwcA==',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip,deflate',
    'isToken': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '55',
    'proxy_method': 'POST',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app:'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    au_dict=json.loads(response.text)
    return au_dict
def getmessage(name,password):
    au_dict=renzheng(name,password)
    url = "http://dcmx.tjdz.net/admin/sysstudent/findStudentByUserId/"+str(au_dict['user_id'])
    payload={}
    headers = {
    'Host': 'dcmx.tjdz.net',
    'Content-Type': 'application/json;charset=UTF-8',
    'Connection': 'keep-alive',
    'proxy_method': 'GET',
    'Accept': '*/*',
    'TENANT-ID': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
    'Authorization': 'Bearer '+str(au_dict['access_token']),
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data=json.loads(response.text)['data']
    data['au']='Bearer '+str(au_dict['access_token'])
    return data
def submit(name,password):
    data=getmessage(name,password)
    url = "http://dcmx.tjdz.net/admin/studentTemperature/submit"

    payload2=[{"location": "天津市天津市津南区雅深路4号",
        "userid": str(data['userid']),
        "status": 0,
        "studentName": data['name'],
        "managerName": "问露",
        "fillDate": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "listTemperature": None,
        "updateTime": None,
        "operatorName": None,
        "latitude": 39.009026963975693,
        "day": None,
        "studentSex": data['sex'],
        "listProcess": [],
        "operatorId": None,
        "id": None,
        "studentId": data['studentid'],
        "num": "36",
        "longitude": 117.3768375651042,
        "healthCode": "",
        "studentSexName": None,
        "className": data['className'],
        "fillStage": 0,
        "deptName": data['collegeName'],
        "statusName": None,
        "itineraryCode": "",
        "createTime": None,
        "cityName": "天津市",
        "fillStageName": None,
        "isSave": None,
        "studentStatus": 1}]

    headers = {
        'Host': 'dcmx.tjdz.net',
        'Content-Type': 'application/json;charset=UTF-8',
        'proxy_method': 'POST',
        'Accept': '*/*',
        'Connection': 'close',
        'TENANT-ID': '1',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
        'Authorization': data['au'],
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate'
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(payload2))
    return data['name']+str(json.loads(response.text)['data'])+'\n'

if __name__ == '__main__':
    people = [[20197009, 'OBEotzUqFePDdjyS16XtqA%3D%3D'], [20197022, 'Dg5XuEVfP8R4%2BAqJsF3D3g%3D%3D'],
              [20197010, 'Dg5XuEVfP8R4%2BAqJsF3D3g%3D%3D'], [20197015, 'OBEotzUqFePDdjyS16XtqA%3D%3D'],
              [20197011, 'Dg5XuEVfP8R4%2BAqJsF3D3g%3D%3D'], [20197012, 'Dg5XuEVfP8R4%2BAqJsF3D3g%3D%3D'],
            [20207017, 'sJgDVbzAraBfPzPinXiGqg==']]
    for peo in people:
        print(submit(peo[0], peo[1]))

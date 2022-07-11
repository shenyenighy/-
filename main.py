import requests
import time
headers = {
    "cookie": '',
    "referer": "https://zhidao.baidu.com/pages/consult/index/grabbing-orders?role=consultor",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44",
    "X-ik-token": "62063cdfb0f9f6da215b3fd82aef0d8f"
}
while True:
    res = requests.get(url="https://zhidao.baidu.com/nchat/api/getorderlist?htj_to=20$514916570092766906469459637416574494460256362&htj_vw=021170451490000000000000000000000000000000000000000000008401ff8003729648425BD5452E73CD874046E009D87:FG=10000000000000&htj_app=universe&listtype=payorder&pn=0&rn=20&verifyCodeDs=&verifyCodeToken=&url=/nchat/api/getorderlist", headers=headers, timeout=5)
    js = res.json()
    if js["data"]["list"] == []:
        print("无单")
    else:
        print("有单")
        for x in js["data"]["list"]:
            aid = x["aid"]
            dySubToken = x["dySubToken"]
            strategyLogId = x["strategyLogId"]
            url = "https://zhidao.baidu.com/nchat/submit/cananswer?replyEntry=pay_zdr_zxzt_order&aid=" + str(aid) + '&htj_to=20$514916570092766906469459637416574505109896242&htj_vw=021170451490000000000000000000000000000000000000000000008401ff8003729648425BD5452E73CD874046E009D87:FG=10000000000000&htj_app=universe&experiment=smallflow_grab_high_value_exp&dySubsidy=50&dySubToken=' + str(dySubToken) + '&recReasonType=1&strategyLogId='+ str(strategyLogId)
            res = requests.get(url=url, headers=headers)
            print(res.json())
    time.sleep(0.8)

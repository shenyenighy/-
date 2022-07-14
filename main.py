import requests
import aiohttp
import time
import asyncio
urls = []
headers = {
    "cookie": 'PSTM=1657204393; BIDUPSID=BF36C9FF991F112D75DD1865B337DFBA; MCITY=-300:; BAIDUID=29648425BD5452E73CD874046E009D87:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZFY=:AF1MJAN5qX4qmyBxD1YJJxpr3efpsrVR:AKch3tKVrEs:C; session_id=1657782429863698026137061347; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1657539504,1657542075,1657621520,1657782431; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1657782431; ab_sr=1.0.1_YmRlYWI2NjI2NTZjMTUzMGQ4Nzg3OGRjZTE1Y2QzMTI2OTlhZGJhZDBmMGQxZGZkZWM1MTM5NzU4YjU4ODA0OGU3OWUyMmJiOWE3MGMyZTMxNzc4NGU0N2NmMzM4ODIyZjY0MDg5ODgxMGExNjFmOTJlNzBiNGJiNTIxOTQ1MTdkN2Y4MzkwMDIxM2EyMTU2YjhhMTZjNTliZDFhZmYzZWZhY2E1MDQ2MTVmNzc1NjA4ZjAxMGQ0NDExNGZjZDRk; shitong_key_id=2; shitong_data=6203e0ed864489f09759c00eba3ca7923215848bb70750654d9c4411b296750a49d2c7749996b93d0c58b8a0608718a64792e5e5df096bd2b752e1730b6da3217dc77dd86e688caeae01b378f63ade5e3adde3f2edf537ada6005cec5824b031; shitong_sign=1e873b78; ZD_ENTRY=empty; BDUSS=k3TzJxQ3RoY0dSRzVOYjdDWTVkai1tcGtwUFF5SWFwZFBCendlbEFISWlUdmRpRVFBQUFBJCQAAAAAAAAAAAEAAADCdhVUc3TJ7tK5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACLBz2Iiwc9iYX; BDUSS_BFESS=k3TzJxQ3RoY0dSRzVOYjdDWTVkai1tcGtwUFF5SWFwZFBCendlbEFISWlUdmRpRVFBQUFBJCQAAAAAAAAAAAEAAADCdhVUc3TJ7tK5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACLBz2Iiwc9iYX',
    "referer": "https://zhidao.baidu.com/pages/consult/index/grabbing-orders?role=consultor",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 Edg/103.0.1264.44",
    "X-ik-token": "62063cdfb0f9f6da215b3fd82aef0d8f"
}
def geturl():
    while True:
        res = requests.get(url="https://zhidao.baidu.com/nchat/api/getorderlist?htj_to=20$514916570092766906469459637416574494460256362&htj_vw=021170451490000000000000000000000000000000000000000000008401ff8003729648425BD5452E73CD874046E009D87:FG=10000000000000&htj_app=universe&listtype=payorder&pn=0&rn=20&verifyCodeDs=&verifyCodeToken=&url=/nchat/api/getorderlist", headers=headers, timeout=5)
        js = res.json()
        if not js["data"]["list"]:
            print("无单")
        else:
            print("有单")
            for x in js["data"]["list"]:
                aid = x["aid"]
                dySubToken = x["dySubToken"]
                strategyLogId = x["strategyLogId"]
                url = "https://zhidao.baidu.com/nchat/submit/cananswer?replyEntry=pay_zdr_zxzt_order&aid=" + str(aid) + '&htj_to=20$514916570092766906469459637416574505109896242&htj_vw=021170451490000000000000000000000000000000000000000000008401ff8003729648425BD5452E73CD874046E009D87:FG=10000000000000&htj_app=universe&experiment=smallflow_grab_high_value_exp&dySubsidy=50&dySubToken=' + str(dySubToken) + '&recReasonType=1&strategyLogId='+ str(strategyLogId)
                urls.append(url)
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())
                time.sleep(0.9)
async def catch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            print(await resp.json())
async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(catch(url))
        tasks.append(task)
    await asyncio.wait(tasks)
if __name__ == "__main__":
    geturl()

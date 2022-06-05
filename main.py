'''
Author: Travis CI travis@travis-ci.org
Date: 2022-06-05 17:58:45
LastEditors: Travis CI travis@travis-ci.org
LastEditTime: 2022-06-05 18:29:22
FilePath: \c:Users\morni\OneDrive - 晨飛\桌面\morningfly的機器人\bot.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import json
ipp = input()
api = requests.get("http://ip-api.com/json/"+ipp)
api2 = requests.get("https://api.mcsrvstat.us/2/"+ipp)
jsons = json.loads(api.text)
jsons2 = json.loads(api2.text)
print("伺服器真實IP：\t"+jsons["query"])
print("伺服器Port：\t"+str(jsons2["port"]))
print("上線人數：\t"+str(jsons2["players"]["online"]))
print("最大人數：\t"+str(jsons2["players"]["max"]))
print("SRV紀錄：\t"+str(jsons2["debug"]["srv"]))
print("是否還活著：\t"+str(jsons2["debug"]["ping"]))
print("城市：\t"+jsons["city"])
print("國家：\t"+jsons["country"]+","+jsons["regionName"]+","+jsons["city"])
print("電信提供商ISP：\t"+jsons["isp"])
print("組織：\t"+jsons["org"])
print("AS編號：\t"+jsons["as"])

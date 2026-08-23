#查天气脚本
import requests
#请求一个公开的天气api
response = requests.get("https://wttr.in/Beijing?format=%C+%t")
weather = response.text
print(f"北京的天气：{weather}")


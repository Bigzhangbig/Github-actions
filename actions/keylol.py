import requests, json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

s = requests.Session()

token = ""
if token == "":
    token = input().strip()

def main():
    # 签到返回链接
    url = f'https://keylol.com/home.php?mod=spacecp'
    headers = {
        "sec-fetch-mode": "same-origin",
        "dnt": "1",
        "accept-encoding" : "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "cache-control": "max-age=0",
        "cookie": token
    }
    response = s.get(url, headers=headers)
    if (response.status_code == 200):
        logger.info("keylol - 签到成功！🎉")
    else:
        logger.error("keylol - 签到失败")

if __name__ == "__main__":
    main()
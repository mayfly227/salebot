import requests

from config import msg_config
from log import botLog

headers = {
    'Content-Type': 'application/json',
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36',

}


def send_group_msg(group_id, message, auto_escape=False):
    data = {
        "group_id": group_id,
        "message": message,
        "auto_escape": auto_escape
    }
    try:
        res = requests.post(msg_config.get("send_group_msg"), json=data,timeout=30)
        if res.json().get("status") == "ok":
            botLog.info(f"转发到{group_id}---<<<成功!!!>>>{message[:10]}")
        else:
            botLog.info(f"转发到{group_id}---<<<失败!!!>>>(其它原因){message[:10]}")
    except:
        botLog.info(f"转发到{group_id}---<<<失败!!!>>>(超时){message[:10]}")

if __name__ == '__main__':
    send_group_msg("644919551", "test")

# 检查已经损坏的链接
import re
import requests
from pathlib import Path

# 正则匹配 [文字](链接)
link_pattern = re.compile(r"\[.*?\]\((.*?)\)")
# 正则匹配 ![图片说明](图片地址)
img_pattern = re.compile(r"!\[.*?\]\((.*?)\)")


def extract_links_and_imgs(md_text: str):
   
    all_links = link_pattern.findall(md_text)
    all_imgs = img_pattern.findall(md_text)
    return all_links, all_imgs
#findall 一次性扫描所有有用文本并且形成一个列表，括号里面写被扫描文本

def is_broken_link(url: str, timeout: int = 3):

    # 不是http开头 则 本地相对路径图片，直接判断文件是否存在
    if not url.startswith(("http://", "https://")):
        return not Path(url).exists()

    # 网络链接，发请求测试是否可访问
    try:
        # head请求，只拿响应头，不下载完整内容，速度更快
        resp = requests.head(url, timeout=timeout, allow_redirects=True)
        # 状态码 >=400 代表捕获到了一些典型的网络错误
        return resp.status_code >= 400
    except Exception:
        # 超时、连不上、域名不存在
        return True
#和爬虫有部分同理

def check_file_links(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    links, imgs = extract_links_and_imgs(content)

    broken_links = [u for u in links if is_broken_link(u)]
    broken_imgs = [u for u in imgs if is_broken_link(u)]
    return broken_links, broken_imgs

#单独调用可以测试通过识别_main_
if __name__ == "__main__":
    bl, bi = check_file_links("./demo/test1.md")
    print("失效链接：", bl)
    print("损坏图片：", bi)

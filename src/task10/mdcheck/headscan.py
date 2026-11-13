# 扫描题目写入
import re

head1= re.compile(r"^(#{1,6})\s+(.*)$")
# 识别#1-6个是第一组，然后还有这一行剩下的是第二组，是正则表达式

def extract_headings(filepath: str):
    headings = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # 去掉每行首尾空白，再匹配正则
            match_res = head1.match(line.strip())
            if match_res:
                level = len(match_res.group(1))  # #数量就是层级：# →1，##→2
                title_text = match_res.group(2)
                headings.append((level, title_text))
    return headings


def build(headings):

    headlines = []
    for lv, title in headings:
        indent = "  " * (lv - 1)#根据层级决定空格数量以展现出标题级数
        headlines.append(f"{indent}- {title}")#转换成了文本块
    return "\n".join(headlines)

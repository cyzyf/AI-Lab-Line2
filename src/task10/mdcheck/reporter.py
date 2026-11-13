# 一起输出一次
def gen_report(file_info_list, out_path: str = "report.md"):
    
    report_lines = ["# Markdown 文档检查报告\n"]

    for info in file_info_list:
        report_lines.append(f"## {info['file']}")#辨别标签类型
        report_lines.append("### 自动生成目录")
        report_lines.append(info["toc"])

        report_lines.append("### 失效链接")
        if info["broken_links"]:
            for link in info["broken_links"]:
                report_lines.append(f"- 失效 {link}")
        else:
            report_lines.append("-  没有失效链接")

        report_lines.append("### 损坏图片")
        if info["broken_imgs"]:
            for img in info["broken_imgs"]:
                report_lines.append(f"- 损坏 {img}")
        else:
            report_lines.append("-  没有损坏图片")

        report_lines.append("\n---\n")

    # 把列表全部拼接成一个大字符串，写入文件
    full_text = "\n".join(report_lines)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    return out_path


# 模块单独测试入口
if __name__ == "__main__":
    test_data = [
        {
            "file": "./demo/test1.md",
            "toc": "- 一级标题\n  - 二级标题",
            "broken_links": ["https://fake-404.com"],
            "broken_imgs": ["./noimg.png"]
        }
    ]
    res_file = gen_report(test_data, "test_report.md")
    print(f"测试报告已经生成：{res_file}")

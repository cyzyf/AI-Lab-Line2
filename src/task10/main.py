# main.py
import argparse
from mdcheck.scanner import scan_md_files
from mdcheck.toc_builder import extract_headings, build
from mdcheck.link_checker import check_file_links
from mdcheck.reporter import gen_report


def main():
    parser = argparse.ArgumentParser(description="Markdown文档检查清洗CLI工具：扫描md、生成目录、检测坏链接坏图")
#作为工程化的东西，在使用该命令的时候能够出现解释文本
    parser.add_argument("--dir", "-d", required=True, help="待扫描的文件夹路径")
#添加运行命令需要的参数信息
    parser.add_argument("--output", "-o", default="report.md", help="输出报告md文件名称")

    args = parser.parse_args()
#读取一下终端的参数数据打包
    md_path_list = scan_md_files(args.dir)
 #调用scanner文件扫描那些是md
    all_result = []

    for file_path in md_path_list:
        # 提取标题 + 生成目录
        heading_list = extract_headings(file_path)
        headtext = build(heading_list)
        # 检测失效链接、损坏图片
        broken_links, broken_imgs = check_file_links(file_path)

        # 打包成字典，放进结果列表,方便处理
        all_result.append({
            "file": file_path,
            "toc": headtext,
            "broken_links": broken_links,
            "broken_imgs": broken_imgs
        })

    report_path = gen_report(all_result, args.output)
    print(f"全部检查完成！报告输出到：{report_path}")


if __name__ == "__main__":
    main()


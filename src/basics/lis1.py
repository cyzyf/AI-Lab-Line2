# 文件
from pathlib import Path
import json


def scan_md_files(target_dir: str):
    root = Path(target_dir)
    result = {}

    for md_path in root.rglob("*.md"):#遍历
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                line_count = len(lines)#收录信息
                content = "".join(lines)
                char_count = len(content)  # 统计字符（含标点，符合文本字数常规统计）

            rel_path = str(md_path.relative_to(root))
            result[rel_path] = {
                "line_count": line_count,
                "char_count": char_count
            }
        except Exception as e:#读取错误类型后可以直接报错
            rel_path = str(md_path.relative_to(root))
            result[rel_path] = {"error": f"读取失败: {str(e)}"}

    return result


if __name__ == "__main__":
    scan_folder = Path(".")
    stats_data = scan_md_files(scan_folder)

    out_file = Path("summary.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(stats_data, f, ensure_ascii=False, indent=2)

    print(f"统计完成，结果已写入 {out_file.name}")

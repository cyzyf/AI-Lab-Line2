from pathlib import Path
def scan_md_files(thedir: str):#str属于类型注解，可以给人看提示，不具备强行筛选
    p = Path(thedir)
    if not p.exists():
        raise FileNotFoundError(f"目录不存在：{thedir}")
    md_files = list(p.rglob("*.md"))
    return [str(f) for f in md_files]

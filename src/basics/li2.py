#练习2

def dicta():
    student = {
        "name": "lisi",
        "age": 19,
        "score": 88
    }
    print("原始字典：", student)

    print("name:", student.get("name"))#get不容易报错
    print("gender，指定默认值：", student.get("gender", "unknown"))

    student["gender"] = "male"#增
    student["score"] = 92
    print("新增+修改后字典：", student)

    sdict = {"math": 80, "english": 90, "python": 95}
    hscore = {k: v for k, v in sdict.items() if v >= 90}#推导式
    print("推导式筛选90分以上科目：", hscore)

    del student["age"]#删
    print("删除age后的字典：", student)


def seta():
    raw_data = [1, 2, 2, 3, 3, 3, 4]
    data_set = set(raw_data)
    print("\n集合去重结果：", data_set)

    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    print("交集 &：", s1 & s2)
    print("并集 |：", s1 | s2)
    print("差集 s1 - s2：", s1 - s2)


if __name__ == "__main__":
    dicta()
    seta()

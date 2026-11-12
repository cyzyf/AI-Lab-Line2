
#练习1


def lista():
    nu= [1, 2, 3, 4, 5]
    print("原始列表：", nu)#初始化

    nu.append(6)#追加
    nu.insert(0, 0)#插入
    print("追加+插入后：", nu)

    nu[2] = 99
    print("修改下标2元素:", nu)

    slice = nu[1:4]
    print("切片 [1:4]:", slice)

    lists = [x for x in nu if x % 2 == 0]#推导式
    print("推导式筛选偶数：", lists)

    del nu[0]
    nu.pop()
    print("删除后的列表：", nu)#删除


def tuples():
    ituple = ("zhangsan", 20, "student")
    print("\n元组内容:", ituple)
    print("元组下标1:", ituple[1])

    tuple1 = ituple[:2]
    print("元组切片[:2]:", tuple1)

    tuple2 = (1, [2, 3])
    tuple2[1].append(4)
    print("内含列表的元组修改后：", tuple2)


if __name__ == "__main__":#文件还是交互式
    lista()
    tuples()

# 生成fofa语法
# 实现简单的功能,这是支持IP，后续会添加
# 20220922
# charis

import files

def ip():

    #每次运行重置

    result = ""
    files.saveFile("D:\\code\\python\\datasorting\\src\\result.txt", "w", "")

    with open("D:\\code\\python\\datasorting\\src\\ip.txt", "r", encoding="utf-8") as f:

        for i in f.readlines():
            result += 'ip="'+i.strip("\n")+'"'+"\n"


    with open("D:\\code\\python\\datasorting\\src\\result.txt", "a") as f:
        f.write(result)


if __name__ == '__main__':
    ip()
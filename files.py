# 实现文件操作
# 20220922
# charis

def saveFile(path, mode, contens):
    #path 传入写入地址
    #写入文件
    #返回值空
    with open(path, mode, encoding="utf-8") as f:
        f.write(contens)


if __name__ == '__main__':
    saveFile()
import files

# 处理fofa导出的数据
def urlFormatfofa():
    #fofa导出的数据http和http都是区分好的，比较好处理
    # 重置
    # 每次运行重置
    files.saveFile("D:\\code\\python\\datasorting\\result\\https.txt", "w", "")
    files.saveFile("D:\\code\\python\\datasorting\\result\\http.txt", "w", "")

    with open("D:\\code\\python\\datasorting\\src\\url.txt", "r") as f:

        for i in f.readlines():
            if i.strip("\n")[0:5].lower() == "https":
                # https数据写入
                with open("D:\\code\\python\\datasorting\\result\\https.txt", "a") as s:
                    s.write(i)
            elif i.strip("\n")[0:5].lower() != "https" or i.strip("\n")[0:4].lower() == "http":
                # http数据写入
                with open("D:\\code\\python\\datasorting\\result\\http.txt", "a") as z:
                    z.write("http://" + i)
            else:
                pass

# 处理goby插件导出的数据
def urlFormatgoby():
    #goby输出比较有特色主要主机和端口号是分开的
    #使用的过程需要添加gobyhost.txt和gobyport.txt文件到src文件中
    # 重置
    # 每次运行重置
    print("gobying....")
    files.saveFile("D:\\code\\python\\datasorting\\result\\http.txt", "w", "")
    files.saveFile("D:\\code\\python\\datasorting\\result\\https.txt", "w", "")

    with open("D:\\code\\python\\datasorting\\src\\url.txt", "r") as f:
        ips = f.readlines()
    with open("D:\\code\\python\\datasorting\\src\\port.txt", "r") as z:
        ports = z.readlines()

    for ip, port in zip(ips, ports): #合并一起
        for listport in port.split(","):#多个端口转成列表用于分配个循环
            urls = ip.strip("\n") + ":" + listport.strip('\n')
            if urls[0:7].lower() != "http://":
                http = "http://" + urls
                with open("D:\\code\\python\\datasorting\\result\\http.txt", "a") as z:
                    z.write(http + '\n')

    with open("D:\\code\\python\\datasorting\\result\\http.txt", "r") as h:
        for i in h.readlines():
            url = i.strip('\n')
            n = url.rfind(':')
            port = url[n + 1:len(url)]
            if port == "443":
                url = url[0:n] #去除端口号
                if url[0:7].lower() == "http://":
                    with open("D:\\code\\python\\datasorting\\result\\https.txt", "a") as z:
                        https = url.replace('http://', 'https://')
                        z.write(https + '\n')











if __name__ == '__main__':
    urlFormatgoby()
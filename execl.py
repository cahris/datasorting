#读取fadaogo excel获取的数据输出
# 20220922
# charis

import xlrd
import xlwt
import files

def readSheet():


    #重置
    #每次运行重置
    files.saveFile("D:\\code\\python\\datasorting\\src\\excelhttp.txt", "w", "")
    
    wb = xlrd.open_workbook("D:\\code\\python\\datasorting\\src\\test.xlsx")
    # 读取多次工作表中多行数据
    book = xlwt.Workbook()
    sheet = book.add_sheet('fofago全部数据整理')  # 创建一个工作表
    for Sheet in wb.sheet_names():  # 控制sheet
        print("当前Sheet>", Sheet.strip('\n'))
        sh = wb.sheet_by_name(Sheet.strip('\n'))
        # 读取单个工作表中多行数据
        for row in range(1, sh.nrows):
            print("第" + str(row) + "行 第" + str(0) + "列 数据正在提取中", sh.cell(row, 0).value) #只读取url

            with open("D:\\code\\python\\datasorting\\src\\excelhttp.txt", "a") as f:
                if str(sh.cell(row, 0).value).lower()[0:4] == "http":
                    f.write(str(sh.cell(row, 0).value)+"\n")


if __name__ == '__main__':
    readSheet()
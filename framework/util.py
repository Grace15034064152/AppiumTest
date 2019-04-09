import xlrd
import os.path
from framework.logger import Logger
logger=Logger("logger=Util").getlog()
class Util:
    path=os.path.dirname(os.path.abspath("."))
    print(path)
    ex_path=os.path.join(path,"data\data.xlsx")
    print(ex_path)
    @classmethod
    def read_excel(self,excel_path,sheet_name="sheet"):
        """将Execl表格中的数据读取出来:
                 思路：先读行，再读列，以列表字典方式进行数据存储
                 如：[{'username':'test1','password':'123456'},{'username':'test2','password':'123456'}]
        """
        workbook=xlrd.open_workbook(excel_path) #打开workbook
        sheet=workbook.sheet_by_name(sheet_name) #得到表名
        # 获取第一行作为key值
        keys=sheet.row_values(0)
        #得到行
        row=sheet.nrows
        #得到列
        col=sheet.ncols
        if row<1:
            logger.error("行数小于1")

        else:
            l=[]
            for i in range(1,row):
                dic={}
                values=sheet.row_values(i)  #得到每一行的值
                for j in range(0,col):
                    dic[keys[j]]=values[j]
                l.append(dic)
        return l
if __name__=="__main__":
    l=Util.read_excel("E:/pythonWorkplace/AppiumTest/data/data.xlsx", "Sheet1")
    print(l)
    print(l[0]["name"])
    print(l[0]["password"])








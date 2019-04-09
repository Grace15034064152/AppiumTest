import unittest
import HTMLTestRunner
import os
from testsuites.test_search import TestSearch
from testsuites.test_modify import TestModify

#设置报告路径
cur_dir=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(cur_dir,"test_report")
if not os.path.exists(report_path):os.mkdir(report_path)
print(report_path)

#构建测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestModify))
suite.addTest(unittest.makeSuite(TestSearch))


#运行并生成报告
if __name__=="__main__":

    HTML_report=report_path+r"\report.html"
    fp=open(HTML_report,"wb")
    htmlrunner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="测试用例情况")

    # runner=unittest.TextTestRunner(verbosity=2)
    htmlrunner.run(suite)
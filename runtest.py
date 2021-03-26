import unittest
from test_report.HTMLTestRunner import HTMLTestRunner
import time
import os

# 定义输出的文件位置和名字
DIR = os.path.dirname(os.path.abspath(__file__))
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

filename = now + "report.html"
# discover方法执行测试套件
testsuite = unittest.defaultTestLoader.discover(
    start_dir='./testsuites',
    pattern='*case.py',
    top_level_dir=None
)

with open(DIR + '/test_report/' + filename, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='gateway UI report',
        description='执行情况',
        tester='tester'
    )
    runner.run(testsuite)
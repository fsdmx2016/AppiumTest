from selenium import webdriver
import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        # path = "/Users/sunpeng/documents/chromedriver"  # 注意这个路径需要时可执行路径（chmod 777 dir or 755 dir）
        # driver = webdriver.Chrome(executable_path=path)

        self.driver = webdriver.Chrome( "/Users/sunpeng/documents/chromedriver")  # 驱动浏览器
        self.driver.implicitly_wait(10)  # 设置隐式等待
        self.driver.maximize_window()  # 最大化浏览器

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
# coding: UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCOD"
# 调用Chrome浏览器，会启动浏览器浏览
# driver = webdriver.Chrome(executable_path="D:\driver\chromedriver_win32\chromedriver.exe")
# 调用phantomjs浏览，不会启动显示页面
driver = webdriver.PhantomJS(executable_path="D:\driver\phantomjs-2.1.1-windows\\bin\phantomjs.exe")
driver.get(url)
# 通过id查找元素
driver.find_element_by_id("txt_2_value1").send_keys("data")
# 通过js查找元素
driver.execute_script("document.getElementById('btnSearch').click()")
# 切换iframe
driver.switch_to_frame("iframeResult")
# 打印页面代码
print(driver.page_source)

# 使用urllib访问页面
# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', url)
# content = r.data.decode("utf-8")
# print(content)
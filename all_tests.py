#coding=utf-8
import sys
sys.path.append(r"D:\code\appium_python\testcase")
sys.path.append(r"D:\code\appium_python\testcase\public")
import unittest
import acfun_app
import HTMLTestRunner
import time

#当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

testunit =  unittest.TestSuite()

#测试用例放入测试套件
testunit.addTest(unittest.makeSuite(acfun_app.Acfun))

#定义报告存放路径
filename =  "D:\\code\\appium_python\\report\\"+unicode(now,'utf-8')+"result.html"
fp = file(filename, 'wb+')


runner = HTMLTestRunner.HTMLTestRunner(

	stream  = fp,
	title = u'acfun_app测试用例',
	description = u'测试用例执行情况'
	)


runner.run(testunit)
#coding=utf-8

import os

#启动模拟器
def emulator_start():
	os.system("emulator @test001")

#启动appium
def appium_start():
	os.system("appium ")

#安装app
def install_app():
	os.system("")

#查看app信息
def app_information(file):
	os.system("aapt dump badging file")



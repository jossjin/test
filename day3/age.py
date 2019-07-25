#! /usr/local/bin/python3


def pdage(age):
	print("请输入年龄【1-50】")
	a = int(input("请输入："))
	if a <= 10:
		print("少年")
	elif a > 10 and a <= 30:
		print("青年")
	elif a > 50:
		raise Exception("sdf",a)
try:
	pdage("asdf")
except Exception as eee:
	print("输入错误！",eee.args[1])
finally:
	print("final")

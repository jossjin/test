#! /usr/local/bin/python3

import sys

def mydeco(r):
	'sadfds端上来克己复礼开始的'
	def run(who):
		'''sdf理
		sdfk
		lsjdfl
			lsdjfjk
		洛杉矶的弗兰克工 i 个 i 个 i 个'''
		print("start run")
		r(who);
		print("end run")
	return run

@mydeco
def myfunc(who):
	'sadfsadfkjjsahd'
	print("my run", who)

#myfunc("joss")
#help(myfunc)
#print(myfunc.__doc__)


#sys.path.append("/home")
#print(sys.path)
#print(__doc__)
#print(__file__)
#print(__name__)

if __name__ == "__main__":
	myfunc("joss")
else:
	print("import deco")

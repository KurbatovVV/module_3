l=[1,4,1,6,"hello","5", "hello"]
l_uniq=[]
for i in l:
	if i not in l_uniq:
		l_uniq.append(i)
		print (l_uniq)
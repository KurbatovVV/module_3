from random import randint
n=5
massive=[[randint(0,100) for i in range(n)] for j in range(n)]
max=0
for i in range(5):
	for j in range(5):
		if (massive[i][j]>max):
			max=massive[i][j]
for i in range(n):
	
	print (massive[i])
print (max)




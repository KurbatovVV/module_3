import json
def register():
	data={'login': 'passwd'}
	secret_info='2022'
	login=input("Введите логин ")
	passwd=input("Введите пароль ")
	if login in data.keys():
		if data[login]==passwd:
			print ("Успешный вход")
			print (secret_info)


		
		with open('password.json', 'w') as f:
			json.dump(data, f)
print(register())
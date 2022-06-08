import json
def login_function():
	#data={'login': 'passwd'}
	secret_info='2022'
	login=input("Введите логин ")
	passwd=input("Введите пароль ")
	with open('password.json', 'r') as f:
			save_login=json.load(f)
	for i in save_login:
		if login==i:
			print ("Успешный вход", secret_info)
		else:
			print("Неверный логин или пароль")


		
		
print(login_function())
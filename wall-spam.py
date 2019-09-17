import vk_api
import time
try:
    log = str(input("login: "))
    pas = str(input("pas: "))
    vk_session = vk_api.VkApi(log, pas, scope='wall,messages')
    vk_session.auth()
    vk = vk_session.get_api()
except:
    print("Неверный Логин или Пароль!")
    time.sleep(2)
    raise

id = str(input("[*] Введите id(0 для себя): "))
if id == "0":
	pp=vk.users.get(v="5.95")
	print(pp)
if 'http' in id:
	id=id.replace("https://vk.com/","")
print("если ввести died, будет убийственное сообщение")
mess = str(input("[*] Введите сообщение: "))
if mess=="died":
    was = "ty."*150
else:
    was=mess
i = 0
kol=int(input("кол-во(0 для безлимита)"))
print(" ")
za=0
za=int(input("задержка(не менее 0):"))
if id==0:
	while i<=kol or kol==0:
		vk.wall.post( message=was)
		i+=1
		print("[!] Пост № " + str(i))
		time.sleep(za)
else:
	try:
		while i<=kol or kol==0:
			vk.wall.post(owner_id=id, message=was)
			i+=1
			print("[!] Пост № " + str(i))
			time.sleep(za)
	except:
		print("\tОшибка, возможные причины:\n\n айди должен быть такого типа: id111111\n стена закрыта\nНеверно указан пароль\n Нет соединения (Инета)")
		print("\n\tПроверьте правильность данных\n\nlogin:{}\npass:{}\nid={}".format(log,pas,id))
		time.sleep(2)
		raise

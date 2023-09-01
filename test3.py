#ให้ทำโปรแกรมป้อนจำนวนเงิน และจำนวนคนทางแป้นพิมพ์ และแสดงผลออกมาว่า
#จำนวนเงิน ???? บาท จำนวนคน ???? คน ต้องหารกันคนละ ???? บาท
#จะให้แสดงผลโดยใช้ Print  ทั้ง 5 แบบ
money = input('ป้อนจำนวนเงิน : ')
person = input('ป้อนจำนวนคน : ')
print('-----------------------------------')
print(f'จำนวนเงิน {float(money):.2f} บาท จำนวนคน {person} คน ต้องหารกันคนละ {float(money)/int(person):.2f} บาท')
print('จำนวนเงิน' ,format(float(money),'.2f'), 'บาท' ,'จำนวนคน' ,person, 'คน' ,'ต้องหารกันคนละ' ,format(float(money)/int(person),'.2f'), 'บาท')
print('จำนวนเงิน ' +str(format(float(money),'.2f'))+ ' บาท' ' จำนวนคน '+person+ ' คน' ' ต้องหารกันคนละ ' + str(format(float(money)/int(person),'.2f'))+ ' บาท')
print("จำนวนเงิน {:.2f} บาท จำนวนคน {} ตน ต้องหารกันคนละ {:.2f} บาท".format(float(money),person,(float(money)/int(person))))
print("จำนวนเงิน %.2f บาท จำนวนคน %s คน ต้องหารกันคนละ %.2f บาท " %(float(money),person,(float(money)/int(person))))
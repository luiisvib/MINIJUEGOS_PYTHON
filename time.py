from datetime import datetime


# print(datetime.now().strftime('%Y-%m-%d %H:%M'))
f=open('tiempo.txt','w')
f.write(datetime.now().strftime('%d %H:%M'))
f.close()

f=open('tiempo.txt','r')
tiempo=f.read()
print(tiempo[3:-1])
f.close()


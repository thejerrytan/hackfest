import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root', host='104.196.149.230', database='hackfest')
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='hackfest')

cursor = cnx.cursor()
data = []
f = open('./c_d.csv', 'r', 1)
count = 0
for line in f:
	user = map(lambda x: None if x.strip('\r\n') == 'NA' else x.strip('\r\n'), line.split(','))
	user[0] = int(user[0])
	# print user
	data.append(tuple(user))
	if len(data) >= 1000:
		try:
			cursor.executemany("INSERT INTO hackfest.user (id, gender, age, race, nationality) VALUES (%s, %s, %s, %s, %s);", data)
			count += 1000
			print("count %d" % count)
		except mysql.connector.errors.IntegrityError as e:
			print e
			print cursor._executed
		cnx.commit()
		data = []
try:
	cursor.executemany("INSERT INTO hackfest.user (id, gender, age, race, nationality) VALUES (%s, %s, %s, %s, %s);", data)
	count += 1000
	print("count %d" % count)
except mysql.connector.errors.IntegrityError as e:
	print e
	print cursor._executed
cnx.commit()
data = []
f.close()
cnx.close()

import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root', host='104.196.149.230', database='hackfest')
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='hackfest')

cursor = cnx.cursor()
data = []
f = open('./c_a.csv', 'r', 1)
count = 0
for line in f:
	user = map(lambda x: None if x.strip('\r\n') == 'NA' else x.strip('\r\n'), line.split(','))
	user[0] = int(user[0]) if user[0] != '' else user[0]
	user[1] = int(user[1]) if user[1] != '' else user[1]
	user[2] = int(user[2]) if user[2] != '' else user[2]
	user[3] = int(user[3]) if user[3] is not None else user[3]
	# (order_id, corporate_id, customer_id, postal_sector)
	# try:
	# 	if user[1] != '':
	# 		cursor.execute("INSERT hackfest.user (id, corporate, postal) VALUES (%s, %s, %s)", (user[1], 1, user[3]))
	# 	else:
	# 		cursor.execute("UPDATE hackfest.user SET corporate=0,postal=%s WHERE id=%s", (user[3],user[2]))
	# 	count += 1
	# 	print("count %d" % count)
	# except mysql.connector.errors.IntegrityError as e:
	# 	print e
	# 	print cursor._executed
	try:
		user_id = user[1] if user[1] != '' else user[2]
		print user_id
		cursor.execute("INSERT hackfest.order (id, user_id, postal_sector) VALUES (%s, %s, %s)", (user[0], user_id, user[3]))
	except mysql.connector.errors.IntegrityError as e:
		print e
	cnx.commit()
f.close()
cnx.close()

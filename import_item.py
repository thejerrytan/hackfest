import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root', host='104.196.149.230', database='hackfest')
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='hackfest')

cursor = cnx.cursor()
data = []
f = open('./o_i.csv', 'r', 1)
count = 0
for line in f:
	order = map(lambda x: None if x.strip('\r\n') == 'NA' else x.strip('\r\n'), line.split(','))
	order[3] = order[3].strip(' ').strip('$')
	if order[3] == '-':
		order[3] == 0
	else:
		try:
			unit_price = float(order[3]) / int(order[2]) # unit price
		except ValueError as e:
			unit_price = 0
			print e
	# try:
	# 	cursor.execute("INSERT INTO hackfest.item (id, unit_price) VALUES (%s, %s);", (order[1], unit_price))
	# 	count += 1
	# 	print("count %d" % count)
	# except mysql.connector.errors.IntegrityError as e:
	# 	print e
	# 	print cursor._executed
	try:
		cursor.execute("INSERT INTO hackfest.order_item (order_id, item_id, qty, sales_amount) VALUES (%s, %s, %s, %s);", order)
		count += 1
		print("count %d" % count)
	except mysql.connector.errors.IntegrityError as e:
		print e
		print cursor._executed
	cnx.commit()
f.close()
cnx.close()

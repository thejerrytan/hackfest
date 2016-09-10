import mysql.connector
from datetime import datetime
import time

# cnx = mysql.connector.connect(user='root', password='root', host='104.196.149.230', database='hackfest')
cnx = mysql.connector.connect(user='root', password='', host='localhost', database='hackfest')

cursor = cnx.cursor()
data = []
f = open('./o_d.csv', 'r', 1)
count = 0
for line in f:
	order = map(lambda x: None if x.strip('\r\n') == 'NA' else x.strip('\r\n').strip(' '), line.split(','))
	order[1] = order[1].strip(' ').strip('$').strip('(').strip(')')
	order[0] = int(order[0])
	order[2] = int(order[2])
	try:
		order[3] = time.strftime('%H:%M:%S', time.strptime(order[3], '%I.%M %p'))
	except Exception as e:
		print e
		continue
	if order[1] == '-':
		order[1] = 0
	else:
		try:
			order[1] = float(order[1].strip(' ').strip('$').strip('(').strip(')'))
		except Exception as e:
			print e
			continue
	if len(order[4]) != 0:
		order[4] = int(order[4])
		interval = order[5]
		try:
			order[5] = interval.split('Between ')[1].split(' and ')[0].strip(' ')
			order[5] = time.strftime('%H:%M:%S', time.strptime(order[5], '%I:%M %p'))
			delivery_end = interval.split('and ')[1].split('(')[0].strip(' ')
			order.append(time.strftime('%H:%M:%S', time.strptime(delivery_end, '%I:%M %p')))
			order.append(int(order[4]) - order[2])
		except Exception as e:
			print e
	else:
		order[4] = None
		order[5] = None
		order.append(None)
		order.append(None)
	order.append(order.pop(0))
	print order
	try:
		cursor.execute("UPDATE hackfest.`order` SET order_discount=%s, order_day=%s, order_time=%s, delivery_day=%s, delivery_start=%s, delivery_end=%s, day_to_deliver=%s WHERE id=\'" + "%s" + "\';", tuple(order))
		# print(cursor.rowcount)
		print(cursor._executed)
		# print(number_of_rows)
		count += 1
		print("count %d" % count)
	except mysql.connector.errors.IntegrityError as e:
		print e
		print cursor._executed
	cnx.commit()
f.close()
cnx.close()

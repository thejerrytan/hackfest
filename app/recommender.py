from datetime import datetime
import time
import numpy as np
import itertools

def build():
	# cnx = mysql.connector.connect(user='root', password='root', host='104.196.149.230', database='hackfest')
	cnx = mysql.connector.connect(user='root', password='', host='localhost', database='hackfest')
	# np.set_printoptions(threshold=np.inf)
	cursor = cnx.cursor()
	data = np.zeros((6855,6855))
	idx_f = open('./item_idx.csv', 'a')
	count = 0
	idx = {}
	order = {} # item_id to index
	inv_order = [] # index to item_id
	try:
		cursor.execute("SELECT id FROM item")
		for (i,) in cursor:
			inv_order.append(i)
			idx[int(i)] = count
			count += 1
		cursor.execute("""SELECT order.id, item_id FROM hackfest.order
			INNER JOIN hackfest.order_item ON order_id = order.id
			ORDER BY id;""")
		for (order_id, item_id) in cursor:
			try:
				order[int(order_id)].append(int(item_id))
			except Exception as e:
				order[int(order_id)] = [int(item_id)]
		for k,v in order.iteritems():
			for (x,y) in itertools.combinations(v, 2):
				try:
					data[idx[x],idx[y]] += 1
				except Exception as e:
					continue
		# Convert back to item ids
		for j in range(0, 6855):
			rank = []
			for k in range(0, 6855):
				if data[j,k] != 0:
					item_y = inv_order[k]
					rank.append((item_y, data[j,k]))
			item_id = inv_order[j]
			rank = reversed(sorted(rank, key=lambda x: x[1]))
			output = [str(item_id)] + [str(x) for x in rank] + ['\n']
			idx_f.write('|'.join(output))
		idx_f.close()
	except mysql.connector.errors.IntegrityError as e:
		print e
		print cursor._executed
	cnx.close()

def get_rec_for_x(x):
	try:
		x = int(x)
	except ValueError as e:
		return {"error": "Invalid item id"}
	ranked = {"items":[]}
	for rec in data[x]:
		ranked["items"].append(
			{"item": int(rec[0]),
			 "score": float(rec[1])
			})
		# print "Item: %d, Score: %.2f" % (int(rec[0]), float(rec[1]))
	return ranked

f = open('./item_idx.csv', 'r')
data = {}
for l in f:
	row = l.split('|')
	row.pop() # remove '\n' character
	item_x = int(row.pop(0))
	data[item_x] = map(lambda x: x.strip('(').strip(')').split(','), row)
f.close()

def main():
	pass

if __name__ == "__main__":
	main()
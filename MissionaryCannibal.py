left = {'M':3, 'C':3}
right={'M':0, 'C':0}
transfer = ['M', 'C', 'MC', 'CC', 'MM']
queue = [[left, right, -1, str(left)+str(right)+str('\n')]]
def check(side):
	if side['M']<0 or side['C']<0 or side['M']>3 or side['C']>3:
		return False
	if side['M']>=side['C']:
		return True
	elif side['M']==0:
		return True
	return False
def finish(right):
	if right['M']==3 and right['C']==3:
		return True
	return False
def fun():
	while True:
		tq = queue[0]
		for op in transfer:
			tl = tq[0].copy()
			tr = tq[1].copy()
			for char in op:
				tl[char] = tl[char] + tq[2]
				tr[char] = tr[char] - tq[2]
			if check(tl) and check(tr):
				newt = [tl, tr, -tq[2], tq[3]+str(tl)+str(tr)+str('\n')]
				queue.append(newt)
				if finish(tr):
					print("DONE")
					print(newt[3])
					return
		queue.pop(0)
fun()

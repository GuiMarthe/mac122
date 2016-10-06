def intercale(p, q, r, v):
	e = v[p:q]
	d = v[q:r]
	d.reverse()
	w = e + d
	i = 0
	j = r - p - 1
	for k in range(p,r + 1):
		if w[i] <= w[j]:
			v[k] = w[i]
			i += 1
		else:
			v[k] = w[j]
			j -= 1
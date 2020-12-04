def parse(line, sep=''):
	for c in sep:
		line = line.replace(c, ' ')
	return [int(x) if x.isdigit() else x for x in line.split()]
low, high, c, passwd = parse(line, '-:')
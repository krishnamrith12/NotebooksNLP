file = open("trainigFiltered.csv")

lines = file.readlines()

print ''.join([ ','.join([line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[5]]) for line in lines])

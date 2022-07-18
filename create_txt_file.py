f = open("input.txt", "a")
f.truncate(0)
for i in range(1, 100001):
    f.write(str(i))
    f.write("\n")
f.close()
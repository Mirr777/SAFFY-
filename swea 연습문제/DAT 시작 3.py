text = "BBQBHCBTS"
dat = [0] * 100
for i in text:
    dat[ord(i)] += 1

print(max(dat))
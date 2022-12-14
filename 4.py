total = 0
while True:
    d_w_trans = input()
    if d_w_trans == "":
        break
    else:
        d_w_trans = d_w_trans.split(" ")
        if d_w_trans[0] == "D":
            total = total + int(d_w_trans[1])
        elif d_w_trans[0] == "W":
            total = total - int(d_w_trans[1])

print(total)
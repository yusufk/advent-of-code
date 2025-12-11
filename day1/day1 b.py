codes = open("day1/day1.txt").read().splitlines()
position = 50
passwd = 0
for code in codes:
    direction = -1 if code[0] == "L" else 1
    clicks = int(code[1:])
    for _ in range(clicks):
        position = (position + direction) % 100
        if position == 0:
            passwd += 1
print("Passes:", passwd)
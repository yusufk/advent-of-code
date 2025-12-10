codes = open("day1.txt").read().splitlines()
start = 50
passwd = 0
for code in codes:
    if code[0] == "L":
        direction = -1
    else:
        direction = 1
    clicks = int(code[1:])
    start += direction * clicks
    while start > 99:
        start -= 100
#        passwd += 1
    while start < 0:
        start += 100
#        passwd += 1
    if start == 0:
        passwd += 1
    print(start)
print("Passes:", passwd)
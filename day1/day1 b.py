codes = open("test.txt").read().splitlines()
position = 50
passwd = 0
for code in codes:
    print(position)
    if code[0] == "L":
        direction = -1
    else:
        direction = 1
    clicks = int(code[1:])
    position += direction * clicks
    while position > 99:
        position -= 100
        passwd += 1
        print(".")
    while position < 0:
        position += 100
        passwd += 1
        print(".")
    if position == 0:
        passwd += 1
        print(".")
print("Passes:", passwd)
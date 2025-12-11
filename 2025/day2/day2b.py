product_ids = open("2025/day2/day2.txt").read().split(',')
print("Product IDs:", product_ids)
invalid_total = 0
for pid in product_ids:
    start_id = pid.split('-')[0]
    end_id = pid.split('-')[1]
    for i in range(int(start_id), int(end_id)+1):
        s = str(i)
        for k in range(1, len(s)//2 + 1):
            if len(s) % k != 0:
                continue
            pattern = s[:k]
            if pattern * (len(s)//k) == s:
                print("Invalid Product Code:", s)
                invalid_total += i
                break
print("Invalid Total for Product IDs is:", invalid_total)
product_ids = open("2025/day2/day2.txt").read().split(',')
print("Product IDs:", product_ids)
invalid_total = 0
for pid in product_ids:
    print("Processing Product ID:", pid)
    start_id = pid.split('-')[0]
    end_id = pid.split('-')[1]
    print("Start ID:", start_id, "End ID:", end_id)
    for i in range(int(start_id), int(end_id) + 1):
        print("Product Code:", str(i))
        #check for repeated digits
        left = str(i)[len(str(i))//2:]
        right = str(i)[:len(str(i))//2]
        if (left==right):
            print("Invalid Product Code:", str(i))
            invalid_total += i
print("Invalid Total for Product IDs is:", invalid_total)
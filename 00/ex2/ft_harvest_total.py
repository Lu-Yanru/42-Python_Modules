def ft_harvest_total():
    total = 0
    weight1 = int(input("Day 1 harvest: "))
    total += weight1
    weight2 = int(input("Day 2 harvest: "))
    total += weight2
    weight3 = int(input("Day 3 harvest: "))
    total += weight3
    print(f"Total harvest: {total}")

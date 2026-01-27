def ft_harvest_total():
    total = 0
    for i in range(1, 4):
        weight = int(input(f"Day {i} harvet: "))
        total += weight
    print(f"Total harvest: {total}")

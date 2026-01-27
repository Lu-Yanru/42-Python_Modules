def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_days(i, days):
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        count_days(i + 1, days)

    count_days(1, days)

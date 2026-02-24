def ft_seed_inventory(seed_type : str, quantity : int, unit : str) -> None :
    print(f"{seed_type} seeds: ", end = "")
    if unit == "packets" :
        print(f"{quantity} {unit} available")
    elif unit == "grams" :
        print(f"{quantity} {unit} total")
    elif unit == "area" :
        print(f"cover {quantity} square meters")

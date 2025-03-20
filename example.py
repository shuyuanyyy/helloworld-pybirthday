import pybirthday

def main():
    """
    Get some birthday-themed visuals.
    """
    cake_str_1 = pybirthday.cake()
    print("Case 1: \n", cake_str_1, sep="")
    
    cake_str_2 = pybirthday.cake("Alice", "Happy 20th Birthday!")
    print("Case 2: \n", cake_str_2, sep="")

    candle_str_1 = pybirthday.candle(3)
    print("Case 3: \n", candle_str_1, sep="")

    candle_str_2 = pybirthday.candle()
    print("Case 4: \n", candle_str_2, sep="")

    balloon_str_1 = pybirthday.balloon(2)
    print("Case 5: \n", balloon_str_1, sep="")
    
    balloon_str_2 = pybirthday.balloon()
    print("Case 6: \n", balloon_str_2, sep="")

    teddy_str_1 = pybirthday.teddy()
    print("Case 7: \n", teddy_str_1, sep="")

    teddy_str_2 = pybirthday.teddy("20th", "Lauren")
    print("Case 8: \n", teddy_str_2, sep="")

if __name__ == "__main__":
    main()

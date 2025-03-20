import pybirthday

def main():
    """
    Get some birthday-themed visuals.
    """
    cake_str_1 = pybirthday.cake()
    print("Case 1: ", cake_str_1)
    
    cake_str_2 = pybirthday.cake("Alice", "Happy 20th Birthday!")
    print("Case 2: ", cake_str_2)

    candle_str_1 = pybirthday.candle(3)
    print("Case 3: ", candle_str_1)

    candle_str_2 = pybirthday.candle()
    print("Case 4: ", candle_str_2)

    balloon_str_1 = pybirthday.balloon(2)
    print("Case 5: ", balloon_str_1)
    
    balloon_str_2 = pybirthday.balloon()
    print("Case 6: ", balloon_str_2)

    teddy_str_1 = pybirthday.teddy()
    print("Case 7: ", teddy_str_1)

    teddy_str_2 = pybirthday.teddy("20th", "Lauren")
    print("Case 8: ", teddy_str_2)

if __name__ == "__main__":
    main()

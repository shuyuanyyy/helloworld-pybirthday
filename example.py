import pybirthday

def main():
    """
    Get some birthday-themed visuals.
    """
    line = pybirthday.cake('Alex', 'Words')
    print(line)

    candle_str_1 = pybirthday.candle(3)
    print("Case 1: ", candle_str_1)

    candle_str_2 = pybirthday.candle()
    print("Case 2: ", candle_str_2)

    balloon_str_1 = pybirthday.balloon(2)
    print("Case 3: ", balloon_str_1)
    
    balloon_str_2 = pybirthday.balloon()
    print("Case 4: ", balloon_str_2)

    teddy_str_1 = pybirthday.teddy()
    print("Case 5: ", teddy_str_1)

    teddy_str_2 = pybirthday.teddy("20th", "Lauren")
    print("Case 6: ", teddy_str_2)

if __name__ == "__main__":
    main()
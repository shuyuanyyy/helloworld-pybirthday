

def cake(name, words):
    return

def candle(n):
    candle_parts = [
        "  )  ",  
        " (()) ",  
        "  )(  ",  
        " (()) ",  
        "  ))  ",  
        "  )   ",  
        "  ^   ",  
        " |||  ",  
        " |||  "
    ]
    result = "\n".join("".join(part for _ in range(n)) for part in candle_parts)
    return result
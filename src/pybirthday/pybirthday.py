

def cake(name, words):
    return

def candle(n: int) -> str:
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
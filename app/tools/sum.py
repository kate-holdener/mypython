def sum(arg):
    try: 
        total = 0
        for val in arg:
            total += val
    except Exception:
        return "Error occured!", 500

    return total

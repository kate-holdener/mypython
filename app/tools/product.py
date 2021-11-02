def product(arg):
    try: 
        total = 1
        for val in arg:
            total *= val
    except Exception:
        return "Error occured!", 500

    return total

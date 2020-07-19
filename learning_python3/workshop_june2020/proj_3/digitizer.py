
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def convert(stmt):
    """
    Converts an iterable representing digits in words format to integers
    """
    try:
        number = ''
        for t in stmt:
            number += DIGIT_MAP[t.lower()]
        number = int(number)
        return number
    except (KeyError, TypeError) as e:
        print(f"Exception handled: {e}")
        raise
    except Exception as e:
        print(f"I don't know want really went wrong. {e}")
        raise


def str_sqrt(stmt):
    """
    Returns sqrt of an iterable representing digits in words format
    """
    number = convert(stmt)
    import math
    return math.sqrt(number)
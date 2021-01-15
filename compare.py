# puryear pg 5
# javascript has comparison (==) and strict comparison (===)
# python only does strict comparison


def compare(a, b):
    "coerce and check equality like javascript"
    type_a = type(a)
    type_b = type(b)
    try:
        if type_a(b) == a:
            return True
    except Exception as e:
        print(e)
    try:
        if type_b(a) == b:
            return True
    except Exception as e:
        print(e)
    return a == b


def strict_compare(a, b):
    "strict comparison without coercion"
    return a == b


if __name__ == "__main__":
    a = 2
    b = "2"
    print(f"a: {type(a)} = {a}")
    print(f"b: {type(b)} = {b}")
    print(f"compare(a,b)", compare(a, b))
    print(f"strict_compare(a,b)", strict_compare(a, b))

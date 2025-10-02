# debug_example.py

def compute_ratio(a, b):
    return a / b  # Potential ZeroDivisionError when b == 0


def main():
    values = [1, 2, 3, 0, 4]
    total = 0
    for v in values:
        total += compute_ratio(10, v)
    print("Total:", total)


if __name__ == "__main__":
    main()
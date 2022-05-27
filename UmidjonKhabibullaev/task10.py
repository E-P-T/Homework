def odd_numbers_generator():
    current = 1
    while True:
        yield current
        current += 2

if __name__ == "__main__":
    nums = odd_numbers_generator()
    for n in nums:
        print(n)
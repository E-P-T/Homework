def get_products(numbers: list[int]) -> list[int]:
    """ Function to calculate the product of all integers except of the integer in given `numbers`,
        for position of which the product is calculating.
        Returns the list of calculated products.
    """
    products = list()
    product = 1
    for number in numbers:
        product *= number

    for number in numbers:
        products.append(int(product / number))

    return products


if __name__ == "__main__":
    print(get_products([3, 2, 1]))
    
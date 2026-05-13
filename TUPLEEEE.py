# Program to calculate the product of all numbers in a given tuple

def tuple_product(t):
    product = 1
    for num in t:
        product *= num
    return product

# Example usage
given_tuple = (1, 2, 3, 4, 5)
result = tuple_product(given_tuple)
print(f"The product of the numbers in the tuple {given_tuple} is {result}")
def check_frequency(text_dict, value):
    """
    Check the frequency of a value in the given text dictionary.
    
    Args:
        text_dict (dict): The dictionary to search in
        value: The value to find the frequency of
        
    Returns:
        int: The number of times the value appears in the dictionary
    """
    frequency = 0
    for v in text_dict.values():
        if v == value:
            frequency += 1
    return frequency


# Example usage
if __name__ == "__main__":
    text_dict = {"a": "apple", "b": "apple", "c": "banana", "d": "apple"}
    value = "apple"
    result = check_frequency(text_dict, value)
    print(f"Frequency of '{value}': {result}")

def safe_read(array, index):
    try:
        # Check if index is within valid range
        if 0 <= index < len(array):
            return array[index]
        else:
            print(f"Warning: Index {index} out of bounds for array of length {len(array)}")
            return None
    except (TypeError, AttributeError):
        print("Error: Invalid array or index type")
        return None
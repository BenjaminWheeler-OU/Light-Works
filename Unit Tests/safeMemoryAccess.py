import array
import numpy as np

class SafeMemoryAccess:
    def __init__(self, structure):
        self.structure = structure
        self.length = len(structure)

    def safe_read(self, index):
        if 0 <= index < self.length:
            value = self.structure[index]
            print(f"Read successful: value at index {index} is {value}")
            return value
        else:
            print(f"Out-of-bounds read attempt at index {index}. Read aborted.")
            return None

    def safe_write(self, index, value):
        if 0 <= index < self.length:
            self.structure[index] = value
            print(f"Write successful: index {index} updated to {value}")
        else:
            print(f"Out-of-bounds write attempt at index {index}. Write aborted.")

# a few test cases to demonstrate how this works (will not be in final code)
def demonstrate_safe_access():
    print("\n--- Demonstrating Safe Access ---")

    # Supported data structures
    data_list = [10, 20, 30, 40]
    data_bytearray = bytearray([1, 2, 3, 4])
    data_array = array.array('i', [100, 200, 300])
    data_ndarray = np.array([9, 8, 7, 6])

    structures = {
        "List": data_list,
        "Bytearray": data_bytearray,
        "Array": data_array,
        "Numpy Array": data_ndarray
    }

    for name, struct in structures.items():
        print(f"\n{name}:")
        accessor = SafeMemoryAccess(struct)
        accessor.safe_write(2, 999)       # Valid
        accessor.safe_read(2)             # Valid
        accessor.safe_write(10, 123)      # Invalid
        accessor.safe_read(-5)            # Invalid

if __name__ == "__main__":
    demonstrate_safe_access()



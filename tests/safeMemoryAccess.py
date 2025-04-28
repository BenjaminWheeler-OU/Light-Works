class SafeMemoryAccess:
    def __init__(self, structure):
        self.structure = structure
        self.length = len(structure)

    def safe_read(self, index):
        if 0 <= index < self.length:
            value = self.structure[index]
            # print(f"Read successful: value at index {index} is {value}")
            return value
        else:
            print(f"Out-of-bounds read attempt at index {index}. Read aborted.")
            return None

    def safe_write(self, index, value):
        if 0 <= index < self.length:
            self.structure[index] = value
            # print(f"Write successful: index {index} updated to {value}")
        else:
            print(f"Out-of-bounds write attempt at index {index}. Write aborted.")
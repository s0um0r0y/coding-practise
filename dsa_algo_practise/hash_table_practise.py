class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key) -> int:
        return sum(ord(char) for char in key) % self.size
    
    def add(self, key, value) -> bool:
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        return True

    def get(self, key) -> None:
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
            return None
        return None
    
    def remove(self, key) -> bool:
        # remove a value
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def print_table(self) -> None:
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: ", end = '')
            for k, v in bucket:
                return print(f"{k}: {v}", end = '')

# Example 
hash_table = HashTable(10)
hash_table.add(1,"Charlotte")
hash_table.add(2,"Thomas")
hash_table.add(3,"Jens")
hash_table.add(4,"Peter")
hash_table.add(5,"Lisa")
hash_table.add(6,"Adele")
hash_table.add(7,"Michaela")
hash_table.add(8,"Bob")

hash_table.print_table()
print(hash_table.get(1))  # Output: Charlotte

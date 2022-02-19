
class HashTable:

    def __init__(self, len):
        self.table = [None ] *len
        self.len = len

    def _hash_function(self, value):
        return value % self.len

    def insert(self, value):
        index = self._hash_function(value)

        if self.table[index] is None:
            self.table[index] = [value]

        self.table[index].append(value)

    def search(self, value_to_find):
        index = self._hash_function(value_to_find)

        for value in self.table[index]:
            if value == value_to_find:
                return True

        return False




if __name__ == '__main__':

    hash_table_len = 9

    values = [1131, 5, 7, 32, 29, 33, 383, 44, 2342, 54, 444, 223, 29443, 3]

    table = HashTable(hash_table_len)
    for value in values:
        table.insert(value)

    value_to_find = 9

    if table.search(value_to_find):
        print('found')
    else:
        print('not found')


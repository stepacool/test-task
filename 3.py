

class Hash_table:
    """
    Сделал через пустые списки из-за коллизий.
    """

    def __init__(self, len):
        self.len = len
        self.table = [[] for x in range(self.len)]

    def make_hash(self, key):
        """
        Способов хешировать огромное множество, выбрал простенький через код знаков.
        """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.len  # Чтобы всегда быть в области длины массива

    def insert(self, key, value):
        intkey = self.make_hash(key)
        self.table[intkey].append([key, value])

    def delete(self, key):
        intkey = self.make_hash(key)
        for item in self.table[intkey]:
            if item[0] == key:
                self.table[intkey].remove(item)
                break

    def search(self, key):
        intkey = self.make_hash(key)
        for item in self.table[intkey]:
            if item[0] == key:
                print(item[1])

    def __str__(self):
        return str(self.table)


if __name__ == "__main__":
    employees = Hash_table(10)
    employees.insert("Vasiliy", "Engineer")
    employees.insert("Peter", "SSM")
    employees.insert("Sergei", "Janitor")
    employees.insert("Nikolai", "Art-director")
    employees.search("Vasiliy")
    employees.search("Peter")
    employees.delete("Vasiliy")
    print(employees)

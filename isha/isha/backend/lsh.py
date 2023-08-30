import random


class LocalitySentitiveHashing:
    """
    class to implement Locality sensitive hashing
    """

    def __init__(self, data, hash_size, seed):
        self.data = data
        self.hash_size = hash_size
        self.seed = seed
        self.hash_tables = []
        self.hash_data()

    def hash_data(self):
        """
        hash the data
        """
        for i in range(self.hash_size):
            hash_table = {}
            for j in range(len(self.data)):
                hash_value = self.hash_vector(self.data[j], i)
                if hash_value in hash_table:
                    hash_table[hash_value].append(j)
                else:
                    hash_table[hash_value] = [j]
            self.hash_tables.append(hash_table)

    def hash_vector(self, vector, i):
        """
        hash the vector
        """
        return hash(tuple(self.random_hyperplane(vector, i)))

    def random_hyperplane(self, vector, i):
        """
        generate random hyperplane
        """
        random.seed((i + 1) * self.seed)
        hyperplane = []
        for value in vector:
            hyperplane.append(random.randint(0, 1))
        return hyperplane

    def query(self, query_data):
        """
        query the data
        """
        candidate_set = set()
        for i in range(self.hash_size):
            hash_value = self.hash_vector(query_data, i)
            if hash_value in self.hash_tables[i]:
                for item in self.hash_tables[i][hash_value]:
                    candidate_set.add(item)
        return candidate_set

    def get_data(self):
        """
        return the data
        """
        return self.data

    def get_hash_tables(self):
        """
        return the hash tables
        """
        return self.hash_tables

    def get_hash_size(self):
        """
        return the hash size
        """
        return self.hash_size

    def get_seed(self):
        """
        return the seed
        """
        return self.seed

    def get_hash_table(self, i):
        """
        return the hash table
        """
        return self.hash_tables[i]

    def get_hash_table_size(self, i):
        """
        return the hash table size
        """
        return len(self.hash_tables[i])

    def get_hash_table_keys(self, i):
        """
        return the hash table keys
        """
        return self.hash_tables[i].keys()


def uniform_hash(key):
    """
    write a hash function without using inbuilt hash function
    """
    seed = 131
    hash_value = 0
    for i in key:
        hash_value = (hash_value * seed) + ord(i)
    return hash_value % 2**32

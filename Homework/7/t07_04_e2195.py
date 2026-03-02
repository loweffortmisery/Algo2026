EMPTY = "Empty"
DELETED = "Deleted"

def is_prime(num):
    if (num < 2): 
        return False
    for i in range(2, int(num**0.5)+1):
        if (num % i == 0):
            return False
    return True


class Set():
    def __init__(self, size_=100000):
        self.size = size_
        self.count = 0
        self.keys = [EMPTY] * self.size



    def hash(self, key):
        M = 1_000_000_007
        N = 31
        h = 0
        for char in key:
            h = (h * N + ord(char)) % M
        return h % self.size

    def rehash(self):
        self.size *= 2
        self.size += 1
        while(not is_prime(self.size)):
            self.size += 2
        _keys = self.keys 
        self.__init__(self.size)
        for key in _keys:
            if (key not in [EMPTY, DELETED]):
                self.add(key)
                

    def add(self, key):
        if self.count > 0.7 * self.size:
            self.rehash()
        i = self.hash(key)
        j = -1
        while (self.keys[i] is not EMPTY):

            if(self.keys[i] is DELETED):
                if (j == -1):
                    j = i
                i = (i+1) % self.size
                continue
            if (self.keys[i] == key):
                return
            i = (i+1) % self.size

        if (j == -1):
            j = i
        self.keys[j] = key
        self.count += 1

    def find(self, key):
        i = self.hash(key)
        while (self.keys[i] is not EMPTY):
            if (self.keys[i] == key):
                return True
            i = (i+1) % self.size
        return False

    def remove(self, key):
        i = self.hash(key)
        while (self.keys[i] is not EMPTY):
            if (self.keys[i] == key):
                self.keys[i] = DELETED
                return
            i = (i+1) % self.size

    def __contains__(self, key):
        return self.find(key)

def split_line(line):
    for char in (".", ",", ":", ";", "-", "'", '"', "!", "?"):
        line = line.replace(char," ")
    return line.split()

def grade_essay(m, dictionary):
    grade = 0
    # 0 - Everything is going to be OK.
    # 1 - Some words from the text are unknown.
    # 2 - The usage of the vocabulary is not perfect.
    used_words = Set()
    for _ in range(m):
        line = split_line(input().lower())
        for word in line:
            if word in dictionary:
                used_words.add(word)
            else:
                grade = 1
                return grade
    if used_words.count != dictionary.count:
        grade = 2
    return grade



if __name__ == "__main__":
    n,m = map(int,input().split())
    dictionary = Set()
    for _ in range(n):
        word = input().lower()
        dictionary.add(word)
    grades = ("Everything is going to be OK.", "Some words from the text are unknown.", "The usage of the vocabulary is not perfect.")
    grade = grade_essay(m, dictionary)
    print(grades[grade])
    

    


    


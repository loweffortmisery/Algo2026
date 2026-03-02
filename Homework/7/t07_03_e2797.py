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
        return (key%M)%self.size

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
        return False

    def remove(self, key):
        i = self.hash(key)
        while (self.keys[i] is not EMPTY):
            if (self.keys == key):
                self.keys = DELETED
                return

if __name__ == "__main__":
    n = int(input())
    NUMBERS = list(map(int, input().split()))
    s = Set()
    for i in range(n):
        s.add(NUMBERS[i])
    print(s.count)

    


    


    


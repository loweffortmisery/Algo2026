
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

EMPTY = "EMPTY"
DELETED = "DELETED"





def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class Hash_table:
    def __init__(self, sz = 11):
        self.size = sz
        self.current_size = 0
        self.keys = [EMPTY for _ in range(self.size)] 
        self.values = [EMPTY for _ in range(self.size)] 

    def hash(self, S: str):
        N = 31
        M = 100007
        h = 0
        for i in range(len(S)):
            h = h * N + ord(S[i])
        return (h % M) % self.size

    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2
        _keys = self.keys
        _values = self.values
        self.__init__(self.size)
        for i in range(len(_keys)):
            if _keys[i] not in (EMPTY, DELETED):
                self.put(_keys[i], _values[i])

    def put(self, key, value):
        if self.current_size > 0.7 * self.size:
            self.rehash()
        current = self.hash(key)
        j = -1
        while self.keys[current] is not EMPTY:
            if self.keys[current] == key:
                self.values[current] = value
                return
            if ((j == -1) and (self.keys[current] == DELETED)):
                j = current
            current = (current + 1) % self.size
        if j == -1:
            j = current
            self.current_size += 1

        self.keys[j] = key
        self.values[j] = value 

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] is not EMPTY:
            if self.keys[current] == key:
                return self.values[current]
            current = (current + 1) % self.size
        return None

    def remove(self, key):
        i = self.hash(key)
        while self.keys[i] is not EMPTY:
            if self.keys[i] == key:
                self.keys[i] = DELETED
                self.values[i] = DELETED
                return None
            i = (i + 1) % self.size
        return None


class table_keys_titles(Hash_table):
    def remove_title(self, title):
        self.remove(title)

    def add_title(self, title):
        self.put(title, True)

    def check_for_title(self, title):
        return (self.get(title) == True)

    def get_all_titles(self):
        titles = []
        for i in range(self.size):
            if self.keys[i] not in (EMPTY, DELETED):
                titles.append(self.keys[i])
        return titles

    def get_all_sorted(self):
        return sorted(self.get_all_titles())


class table_keys_authors(Hash_table):
    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2
        _keys = self.keys
        _values = self.values
        self.__init__(self.size)
        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                author = _keys[i]
                _titles = _values[i].get_all_titles()
                if len(_titles) == 0:
                    continue
                self.put(author, _titles[0])
                new_titles = self.get(author)
                for j in range(1, len(_titles)):
                    new_titles.add_title(_titles[j])

    def put(self, key, value):
        if self.current_size > 0.7 * self.size:
            self.rehash()
        current = self.hash(key)
        while self.keys[current] is not EMPTY:
            if self.keys[current] == key:
                self.values[current].add_title(value)
                return
            current = (current + 1) % self.size
        self.current_size += 1
        self.keys[current] = key
        self.values[current] = table_keys_titles()
        self.values[current].add_title(value)
        
    def add_title(self, author, title):
        self.put(author, title)

    def check_for_title(self, author, title):
        titles = self.get(author)
        if titles is None:
            return False
        return titles.check_for_title(title) 

    def remove_title(self, author, title):
        titles = self.get(author)
        if titles is not None:
            titles.remove_title(title)
        

    def get_sorted_titles_by_author(self, author):
        current = self.hash(author)
        while self.keys[current] is not EMPTY:
            if self.keys[current] == author:
                return self.values[current].get_all_sorted()
            current = (current + 1) % self.size
        return []
        



global library_table

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global library_table
    library_table = table_keys_authors()

def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global library_table
    library_table.add_title(author, title)

def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    global library_table
    return library_table.check_for_title(author, title)


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global library_table
    library_table.remove_title(author, title)


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    global library_table
    return library_table.get_sorted_titles_by_author(author)


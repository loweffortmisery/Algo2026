
"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

EMPTY = "EMPTY"
DELETED = "DELETED"

class Node:
    """ Допоміжний клас вузол таблиці """
    def __init__(self, key: str, value):
        self.key = key
        self.value = value 
        self.next = EMPTY 
        self.valid = True 



def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


class Hash_table:
    def __init__(self, sz = 11):
        self.size = sz
        self.current_size = 0
        self.slots: list[Node | EMPTY] = [EMPTY for _ in range(self.size)] 

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
        _slots = self.slots
        self.__init__(self.size)
        for node in _slots:
            _node = node
            while _node is not EMPTY:
                self.set(_node.key, _node.value)
                _node = _node.next

    def set(self, key, value):
        if self.current_size > 0.7 * self.size:
            self.rehash()
        i = self.hash(key)
        node = self.slots[i]
        while node is not EMPTY:
            if node.key == key:
                node.value = value
                return
            node = node.next

        self.current_size += 1
        new_node = Node(key, value)
        new_node.next = self.slots[i]
        self.slots[i] = new_node

    def get(self, key):
        i = self.hash(key)
        node = self.slots[i]
        while node is not EMPTY:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def remove(self, key):
        i = self.hash(key)

        node = self.slots[i]
        if node is EMPTY:
            return
        if node.key == key:
            self.slots[i] = node.next
            return

        prev = node
        node = node.next
        while node is not EMPTY:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next


class table_keys_titles(Hash_table):
    def remove_title(self, title):
        self.remove(title)

    def add_title(self, title):
        self.set(title, True)

    def check_for_title(self, title):
        return (self.get(title) == True)

    def get_all_titles(self):
        titles = []
        for node in self.slots:
            _node = node
            while _node is not EMPTY:
                titles.append(_node.key)
                _node = _node.next
        return titles

    def get_all_sorted(self):
        return sorted(self.get_all_titles())


class table_keys_authors(Hash_table):
    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2
        _slots = self.slots
        self.__init__(self.size)
        for node in _slots:
            _node = node
            while _node is not EMPTY:
                author = _node.key
                _titles = _node.value.get_all_titles()
                _node = _node.next
                if(len(_titles) == 0):
                    continue
                self.set(author, _titles[0])
                new_titles = self.get(author)
                for j in range(1, len(_titles)):
                    new_titles.add_title(_titles[j])
                

    def set(self, author, title):
        if self.current_size > 0.7 * self.size:
            self.rehash()
        i = self.hash(author)
        node = self.slots[i]
        while node is not EMPTY:
            if node.key == author:
                node.value.add_title(title)
                return
            node = node.next
        self.current_size += 1
        new_node = Node(author, table_keys_titles())
        new_node.value.add_title(title)
        new_node.next = self.slots[i]
        self.slots[i] = new_node
        
    def add_title(self, author, title):
        self.set(author, title)

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
        i = self.hash(author)
        node = self.slots[i]
        while node is not EMPTY:
            if node.key == author:
                return node.value.get_all_sorted()
            node = node.next
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


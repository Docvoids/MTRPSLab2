class CharList:
    class _Node:
        def __init__(self, data: str, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.tail = None
        self.size = 0

    def _validate_char(self, element: str):  # Залишається
        if not isinstance(element, str) or len(element) != 1:
            raise TypeError("Element must be a single character (string of length 1).")

    # Перейменовуємо та адаптуємо _validate_index
    def _validate_index_bounds(self, index: int, for_insert: bool = False):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        if self.size == 0:
            if for_insert and index == 0:
                return
            raise IndexError("Index out of range. List is empty.")

        # Верхня межа для insert - це self.size, для інших - self.size - 1
        upper_bound = self.size if for_insert else self.size - 1

        if not (0 <= index <= upper_bound):
            # Спеціальне повідомлення, якщо upper_bound < 0 (можливо тільки для порожнього списку і for_insert=False)
            actual_upper_display = upper_bound if upper_bound >= 0 else 0
            raise IndexError(f"Index out of range. Must be between 0 and {actual_upper_display}.")

    def _get_node_at(self, index: int) -> _Node:
        # Цей метод передбачає, що індекс вже валідований
        # if index < 0 or index >= self.size: # Додаткова внутрішня перевірка, якщо потрібно
        #      raise IndexError("Internal error: _get_node_at called with invalid index.")
        current = self.tail.next
        for _ in range(index):
            current = current.next
        return current
    def length(self) -> int:
        """Операцію визначення довжини списку."""
        return len(self._data)

    def append(self, element: str) -> None:
        """Операцію додавання елементу в кінець списку."""
        self._validate_char(element)
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        """Операцію вставки елементу на довільну позицію у списку."""
        self._validate_char(element)
        self._validate_index(index, allow_append_pos=True)
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        """Операцію видалення елементу зі списку на вказаній позиції."""
        self._validate_index(index, allow_append_pos=False)
        return self._data.pop(index)

    def deleteAll(self, element: str) -> None:
        """Метод видаляє зі списку усі елементи, які за значенням відповідають шуканому."""
        self._validate_char(element)
        self._data = [item for item in self._data if item != element]

    def get(self, index: int) -> str:
        """Операцію отримання елементу списку на довільній позиції."""
        self._validate_index(index, allow_append_pos=False)
        return self._data[index]

    def clone(self) -> 'CharList':
        """Операцію копіювання списку."""
        new_list = CharList()
        new_list._data = self._data[:]
        return new_list

    def reverse(self) -> None:
        """Операцію обернення списку."""
        self._data.reverse()

    def findFirst(self, element: str) -> int:
        """Операцію пошуку елемента за значенням з голови списку."""
        self._validate_char(element)
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        """Операцію пошуку елемента за значенням з хвоста списку."""
        self._validate_char(element)
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        """Операцію очищення списку."""
        self._data.clear()

    def extend(self, elements: 'CharList') -> None:
        """Операцію розширення списку."""
        if not isinstance(elements, CharList):
            raise TypeError("Can only extend with another CharList instance.")
        for i in range(elements.length()):
            self.append(elements.get(i))

    def __str__(self) -> str: # Оновимо для кільцевого списку
        if self.tail is None:
            return "CharList([])"
        items = []
        current = self.tail.next
        for _ in range(self.size):
            items.append(repr(current.data))
            current = current.next
        return f"CharList([{', '.join(items)}])"

    def __repr__(self) -> str: # Оновимо для кільцевого списку
        if self.tail is None:
            return "CharList(empty)"
        return f"<CharList object with {self.size} elements, tail.data='{self.tail.data}'>"
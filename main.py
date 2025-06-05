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
        return self.size

    def append(self, element: str) -> None:
        """Операцію додавання елементу в кінець списку."""
        self._validate_char(element)
        new_node = self._Node(element)
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        """Операцію вставки елементу на довільну позицію у списку."""
        self._validate_char(element)
        # Валідація індексу для insert дозволяє index == self.size
        self._validate_index_bounds(index, for_insert=True)

        if index == self.size:  # Вставка в кінець (або в порожній список на позицію 0)
            self.append(element)
            return

        new_node = self._Node(element)
        if index == 0:  # Вставка на початок (список не порожній)
            new_node.next = self.tail.next
            self.tail.next = new_node
        else:  # Вставка в середину
            prev_node = self._get_node_at(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.size += 1

    def delete(self, index: int) -> str:
        """Операцію видалення елементу зі списку на вказаній позиції."""
        self._validate_index_bounds(index, for_insert=False)

        deleted_data: str
        if self.size == 1:
            deleted_data = self.tail.data
            self.tail = None
        elif index == 0:
            head = self.tail.next
            deleted_data = head.data
            self.tail.next = head.next
        else:
            prev_node = self._get_node_at(index - 1)
            node_to_delete = prev_node.next
            deleted_data = node_to_delete.data
            prev_node.next = node_to_delete.next
            if node_to_delete == self.tail:
                self.tail = prev_node
        self.size -= 1
        return deleted_data

    def deleteAll(self, element: str) -> None:
        """Метод видаляє зі списку усі елементи, які за значенням відповідають шуканому."""
        self._validate_char(element)
        if self.tail is None:
            return

        temp_storage = []
        current = self.tail.next
        for _ in range(self.size):
            if current.data != element:
                temp_storage.append(current.data)
            current = current.next

        # Зберігаємо оригінальний розмір, щоб знати, чи були зміни
        # original_size = self.size

        self.clear()  # Очищаємо поточний список (скидає self.tail та self.size)
        for char_val in temp_storage:
            self.append(char_val)  # append оновить self.size і self.tail

    def get(self, index: int) -> str:
        """Операцію отримання елементу списку на довільній позиції."""
        self._validate_index_bounds(index, for_insert=False)
        node = self._get_node_at(index)
        return node.data

    def clone(self) -> 'CharList':
        """Операцію копіювання списку."""
        new_list = CharList()
        if self.tail is None:
            return new_list

        current = self.tail.next
        for _ in range(self.size):
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        """Операцію обернення списку."""
        if self.size < 2:
            return

        previous_node = self.tail  # Старий хвіст
        current_node = self.tail.next  # Стара голова
        new_tail_candidate = self.tail.next  # Стара голова стане новим хвостом

        for _ in range(self.size):
            next_node_temp = current_node.next  # Зберігаємо наступний вузол
            current_node.next = previous_node  # Реверсуємо вказівник поточного вузла
            previous_node = current_node  # Рухаємо previous_node вперед
            current_node = next_node_temp  # Рухаємо current_node вперед

        # Після циклу, previous_node вказує на старий хвіст (який тепер нова голова)
        # new_tail_candidate (стара голова) тепер має стати новим хвостом
        self.tail = new_tail_candidate
        # self.tail.next вже вказує на previous_node (нову голову) через останню ітерацію

    def findFirst(self, element: str) -> int:
        """Операцію пошуку елемента за значенням з голови списку."""
        self._validate_char(element)
        if self.tail is None:
            return -1

        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                return i
            current = current.next
        return -1

    def findLast(self, element: str) -> int:
        self._validate_char(element)
        if self.tail is None:
            return -1

        last_found_index = -1
        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                last_found_index = i
            current = current.next
        return last_found_index

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
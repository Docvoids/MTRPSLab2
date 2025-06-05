class CharList:
    def __init__(self):
        self._data = []  # Внутрішній список Python для зберігання даних

    def _validate_char(self, element: str):
        if not isinstance(element, str) or len(element) != 1:
            raise TypeError("Element must be a single character (string of length 1).")

    def _validate_index(self, index: int, allow_append_pos: bool = False):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")

        # Визначаємо верхню межу для індексу
        # Якщо список порожній, upper_bound буде -1 для get/delete, або 0 для insert
        upper_bound = len(self._data) if allow_append_pos else (len(self._data) - 1 if len(self._data) > 0 else -1)

        if len(self._data) == 0:
            if allow_append_pos and index == 0:  # Дозволити вставку в порожній список за індексом 0
                return
            # Для get/delete/insert в порожній список (крім index=0 для insert)
            raise IndexError("Index out of range. List is empty.")

        if not (0 <= index <= upper_bound):
            error_message = f"Index out of range. Must be between 0 and {upper_bound if upper_bound >= 0 else 0}."
            raise IndexError(error_message)

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
        pass

    def get(self, index: int) -> str:
        pass

    def clone(self) -> 'CharList':
        pass

    def reverse(self) -> None:
        pass

    def findFirst(self, element: str) -> int:
        pass

    def findLast(self, element: str) -> int:
        pass

    def clear(self) -> None:
        pass

    def extend(self, elements: 'CharList') -> None:
        pass

    def __str__(self) -> str:
        return f"CharList({self._data})"

    def __repr__(self) -> str:
        return f"CharList({self._data!r})"
import unittest
from custom_list import CharList # Припускаємо, що custom_list.py містить CircularLinkedList реалізацію

class TestCharListCircularLinked(unittest.TestCase):

    def setUp(self):
        self.list = CharList()

    def test_initial_list_is_empty(self):
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail) # Специфічно для кільцевого списку
        self.assertEqual(str(self.list), "CharList([])")

    def test_append_to_empty_list(self):
        self.list.append('a')
        self.assertEqual(self.list.length(), 1)
        self.assertIsNotNone(self.list.tail)
        self.assertEqual(self.list.tail.data, 'a')
        self.assertEqual(self.list.tail.next.data, 'a') # Голова
        self.assertEqual(str(self.list), "CharList(['a'])")

    def test_append_multiple_elements(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'a') # Голова
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.get(2), 'c')
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")

    def test_append_invalid_element(self):
        with self.assertRaises(TypeError):
            self.list.append('ab')
        with self.assertRaises(TypeError):
            self.list.append(1) # type: ignore

    def test_insert_into_empty_list(self):
        self.list.insert('x', 0)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.tail.data, 'x')
        self.assertEqual(self.list.tail.next.data, 'x')
        self.assertEqual(str(self.list), "CharList(['x'])")

    def test_insert_at_beginning(self):
        self.list.append('b')
        self.list.append('c') # ['b', 'c']
        self.list.insert('a', 0) # ['a', 'b', 'c']
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'a') # Нова голова
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")

    def test_insert_at_end(self):
        self.list.append('a')
        self.list.append('b') # ['a', 'b']
        self.list.insert('c', 2) # ['a', 'b', 'c']
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(2), 'c')
        self.assertEqual(self.list.tail.data, 'c') # Новий хвіст
        self.assertEqual(self.list.tail.next.data, 'a')
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")

    def test_insert_in_middle(self):
        self.list.append('a')
        self.list.append('c') # ['a', 'c']
        self.list.insert('b', 1) # ['a', 'b', 'c']
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'a')
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")

    def test_insert_invalid_index(self):
        self.list.append('a')
        with self.assertRaises(IndexError):
            self.list.insert('x', -1)
        with self.assertRaises(IndexError):
            self.list.insert('x', 2) # Довжина 1, допустимий індекс для вставки 0 або 1
        empty_list = CharList()
        with self.assertRaises(IndexError):
            empty_list.insert('x', 1)

    def test_delete_from_single_element_list(self):
        self.list.append('a')
        deleted = self.list.delete(0)
        self.assertEqual(deleted, 'a')
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail)

    def test_delete_first_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c') # ['a', 'b', 'c']
        deleted = self.list.delete(0) # ['b', 'c']
        self.assertEqual(deleted, 'a')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'b')
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'b')

    def test_delete_last_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c') # ['a', 'b', 'c']
        deleted = self.list.delete(2) # ['a', 'b']
        self.assertEqual(deleted, 'c')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.tail.data, 'b')
        self.assertEqual(self.list.tail.next.data, 'a')

    def test_delete_middle_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c') # ['a', 'b', 'c']
        deleted = self.list.delete(1) # ['a', 'c']
        self.assertEqual(deleted, 'b')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.get(1), 'c')
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'a')

    def test_delete_invalid_index(self):
        self.list.append('a')
        with self.assertRaises(IndexError):
            self.list.delete(-1)
        with self.assertRaises(IndexError):
            self.list.delete(1) # Довжина 1, допустимий індекс для видалення 0
        empty_list = CharList()
        with self.assertRaises(IndexError):
            empty_list.delete(0)

    def test_deleteAll_existing_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.list.append('c')
        self.list.append('a') # ['a', 'b', 'a', 'c', 'a']
        self.list.deleteAll('a') # ['b', 'c']
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(str(self.list), "CharList(['b', 'c'])")
        if self.list.length() > 0: # Додано перевірку, щоб уникнути помилки на порожньому списку
            self.assertEqual(self.list.tail.data, 'c')
            self.assertEqual(self.list.tail.next.data, 'b')

    def test_deleteAll_non_existing_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.deleteAll('x')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(str(self.list), "CharList(['a', 'b'])")

    def test_deleteAll_from_empty_list(self):
        self.list.deleteAll('a')
        self.assertEqual(self.list.length(), 0)

    def test_deleteAll_all_elements(self):
        self.list.append('a')
        self.list.append('a')
        self.list.append('a')
        self.list.deleteAll('a')
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail)

    def test_get_element(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.get(1), 'b')

    def test_get_invalid_index(self):
        self.list.append('a')
        with self.assertRaises(IndexError):
            self.list.get(-1)
        with self.assertRaises(IndexError):
            self.list.get(1)
        empty_list = CharList()
        with self.assertRaises(IndexError):
            empty_list.get(0)

    def test_clone_empty_list(self):
        cloned_list = self.list.clone()
        self.assertEqual(cloned_list.length(), 0)
        self.assertIsNone(cloned_list.tail)
        self.assertNotEqual(id(self.list), id(cloned_list))

    def test_clone_non_empty_list(self):
        self.list.append('a')
        self.list.append('b')
        cloned_list = self.list.clone()
        self.assertEqual(cloned_list.length(), 2)
        self.assertEqual(str(cloned_list), "CharList(['a', 'b'])")
        self.assertNotEqual(id(self.list), id(cloned_list))
        # Специфічна перевірка для кільцевого списку: вузли різні
        if self.list.tail and cloned_list.tail:
             self.assertNotEqual(id(self.list.tail), id(cloned_list.tail))
             self.assertNotEqual(id(self.list.tail.next), id(cloned_list.tail.next))

        # Перевірка незалежності
        cloned_list.append('c')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(cloned_list.length(), 3)

        self.list.append('x')
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'x'])")
        self.assertEqual(str(cloned_list), "CharList(['a', 'b', 'c'])")


    def test_reverse_empty_list(self):
        self.list.reverse()
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail)

    def test_reverse_single_element_list(self):
        self.list.append('a')
        self.list.reverse()
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.tail.data, 'a')
        self.assertEqual(self.list.tail.next.data, 'a')

    def test_reverse_multiple_elements(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c') # ['a', 'b', 'c']
        self.list.reverse()   # ['c', 'b', 'a']
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(0), 'c')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.get(2), 'a')
        self.assertEqual(self.list.tail.data, 'a') # Новий хвіст
        self.assertEqual(self.list.tail.next.data, 'c') # Нова голова
        self.assertEqual(str(self.list), "CharList(['c', 'b', 'a'])")

    def test_findFirst_element_present(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.assertEqual(self.list.findFirst('a'), 0)
        self.assertEqual(self.list.findFirst('b'), 1)

    def test_findFirst_element_not_present(self):
        self.list.append('a')
        self.assertEqual(self.list.findFirst('x'), -1)

    def test_findFirst_in_empty_list(self):
        self.assertEqual(self.list.findFirst('a'), -1)

    def test_findLast_element_present(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.list.append('c') # ['a', 'b', 'a', 'c']
        self.assertEqual(self.list.findLast('a'), 2)
        self.assertEqual(self.list.findLast('b'), 1)
        self.assertEqual(self.list.findLast('c'), 3)

    def test_findLast_element_not_present(self):
        self.list.append('a')
        self.assertEqual(self.list.findLast('x'), -1)

    def test_findLast_in_empty_list(self):
        self.assertEqual(self.list.findLast('a'), -1)

    def test_clear_non_empty_list(self):
        self.list.append('a')
        self.list.append('b')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail)

    def test_clear_empty_list(self):
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
        self.assertIsNone(self.list.tail)

    def test_extend_with_non_empty_list(self):
        self.list.append('a') # ['a']
        other_list = CharList()
        other_list.append('b')
        other_list.append('c') # ['b', 'c']
        self.list.extend(other_list) # ['a', 'b', 'c']
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")
        self.assertEqual(self.list.tail.data, 'c')
        self.assertEqual(self.list.tail.next.data, 'a')

        # Перевірка незалежності
        other_list.append('d') # Змінюємо other_list
        self.assertEqual(self.list.length(), 3, "Original list should not change after other_list is modified")
        self.assertEqual(str(self.list), "CharList(['a', 'b', 'c'])")


    def test_extend_with_empty_list(self):
        self.list.append('a')
        empty_other = CharList()
        self.list.extend(empty_other)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(str(self.list), "CharList(['a'])")

    def test_extend_empty_list_with_non_empty(self):
        other_list = CharList()
        other_list.append('b')
        other_list.append('c')
        self.list.extend(other_list)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(str(self.list), "CharList(['b', 'c'])")

    def test_extend_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.list.extend([1, 2, 3]) # type: ignore

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
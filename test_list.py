import unittest
from main import CharList # Припускаємо, що custom_list.py містить ArrayBased реалізацію

class TestCharListArrayBased(unittest.TestCase):

    def setUp(self):
        self.list = CharList()

    def test_initial_list_is_empty(self):
        self.assertEqual(self.list.length(), 0)
        self.assertEqual(str(self.list), "CharList([])")
        self.assertEqual(self.list._data, []) # Специфічна перевірка для цієї реалізації

    def test_append_elements(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['a', 'b'])
        self.assertEqual(str(self.list), "CharList(['a', 'b'])")

    def test_append_invalid_element(self):
        with self.assertRaises(TypeError):
            self.list.append('ab')
        with self.assertRaises(TypeError):
            self.list.append(1) # type: ignore

    def test_insert_into_empty_list(self):
        self.list.insert('x', 0)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list._data, ['x'])

    def test_insert_at_beginning(self):
        self.list.append('b')
        self.list.insert('a', 0)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['a', 'b'])

    def test_insert_at_end(self):
        self.list.append('a')
        self.list.insert('b', 1) # index 1 == length
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['a', 'b'])

    def test_insert_in_middle(self):
        self.list.append('a')
        self.list.append('c')
        self.list.insert('b', 1)
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list._data, ['a', 'b', 'c'])

    def test_insert_invalid_index(self):
        self.list.append('a')
        with self.assertRaises(IndexError):
            self.list.insert('x', -1)
        with self.assertRaises(IndexError):
            self.list.insert('x', 2) # length is 1, so max index for insert is 1
        empty_list = CharList()
        with self.assertRaises(IndexError): # Cannot insert at index 1 if list is empty
            empty_list.insert('x', 1)


    def test_delete_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        deleted = self.list.delete(1) # delete 'b'
        self.assertEqual(deleted, 'b')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['a', 'c'])

    def test_delete_invalid_index(self):
        self.list.append('a')
        with self.assertRaises(IndexError):
            self.list.delete(-1)
        with self.assertRaises(IndexError):
            self.list.delete(1) # length is 1, max index for delete is 0
        empty_list = CharList()
        with self.assertRaises(IndexError):
            empty_list.delete(0)

    def test_deleteAll_existing_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.list.append('c')
        self.list.deleteAll('a')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['b', 'c'])

    def test_deleteAll_non_existing_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.deleteAll('x')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list._data, ['a', 'b'])

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

    def test_clone_list(self):
        self.list.append('a')
        self.list.append('b')
        cloned_list = self.list.clone()
        self.assertEqual(cloned_list.length(), 2)
        self.assertEqual(cloned_list._data, ['a', 'b'])
        self.assertNotEqual(id(self.list._data), id(cloned_list._data)) # Deep copy of _data

        # Test independence
        cloned_list.append('c')
        self.assertEqual(self.list._data, ['a', 'b'])
        self.assertEqual(cloned_list._data, ['a', 'b', 'c'])

    def test_reverse_list(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.list.reverse()
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list._data, ['c', 'b', 'a'])

    def test_reverse_empty_list(self):
        self.list.reverse()
        self.assertEqual(self.list.length(), 0)
        self.assertEqual(self.list._data, [])

    def test_findFirst_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.assertEqual(self.list.findFirst('a'), 0)
        self.assertEqual(self.list.findFirst('b'), 1)
        self.assertEqual(self.list.findFirst('x'), -1)

    def test_findLast_element(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.list.append('c')
        self.assertEqual(self.list.findLast('a'), 2)
        self.assertEqual(self.list.findLast('b'), 1)
        self.assertEqual(self.list.findLast('c'), 3)
        self.assertEqual(self.list.findLast('x'), -1)

    def test_clear_list(self):
        self.list.append('a')
        self.list.append('b')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)
        self.assertEqual(self.list._data, [])

    def test_extend_list(self):
        self.list.append('a')
        other_list = CharList()
        other_list.append('b')
        other_list.append('c')
        self.list.extend(other_list)
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list._data, ['a', 'b', 'c'])
        # Test independence
        other_list.append('d')
        self.assertEqual(self.list._data, ['a', 'b', 'c'])

    def test_extend_with_invalid_type(self):
        with self.assertRaises(TypeError):
            self.list.extend([1,2,3]) # type: ignore

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # exit=False для інтерактивного запуску
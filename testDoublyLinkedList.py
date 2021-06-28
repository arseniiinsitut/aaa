import unittest

from DoublyLinkedList1 import DoublyLinkedList

class DoublyLinkedListTest(unittest.TestCase):

    new_linked_list = DoublyLinkedList()

    new_linked_list.insert_in_emptylist("Zimin")

    new_linked_list.insert_at_start("Kydrashow")

    new_linked_list.insert_at_start("Kuzminskaya")

    new_linked_list.insert_at_start("Vidonchenkov")

    new_linked_list.insert_at_end("Balan")

    new_linked_list.insert_at_end("Fedotov")

    new_linked_list.insert_at_end("Bulgarin")

    new_linked_list.insert_after_item("Zimin", "Muravchenko")

    new_linked_list.insert_before_item("Balan", "Guchev")

    new_linked_list.delete_at_start()

    new_linked_list.delete_at_end()

    new_linked_list.delete_element_by_value("Muravchenko")

    new_linked_list.traverse_list()

if __name__ == '__main__':
    unittest.main()

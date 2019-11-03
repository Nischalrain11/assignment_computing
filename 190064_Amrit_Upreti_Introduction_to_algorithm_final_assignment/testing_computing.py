from computing import *
import unittest


class TestComputing(unittest.TestCase):
    def test_quick_sort(self):
        # test of quick sort that sort the array in the ascending order
        array_to_sort = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                          'BSc. Computing'),
                         (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                          'BSc. Ethical Hacking'),
                         (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                          'BSc. Ethical Hacking')]

        user.combo_sort.set('Id')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('First Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Last Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Contact')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Address')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Date of Birth')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Gender')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Degree')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        # test of quick sort that sort the array in the descending order
        array_to_sort = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                          'BSc. Computing'),
                         (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                          'BSc. Ethical Hacking'),
                         (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                          'BSc. Ethical Hacking')]

        user.combo_sort.set('Id')
        user.radio_descending.invoke()
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('First Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Last Name')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Contact')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Address')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Date of Birth')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Gender')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking')]
        self.assertEqual(array_to_sort, expected_result)

        user.combo_sort.set('Degree')
        user.quick_sort(array_to_sort, 0, len(array_to_sort) - 1)
        expected_result = [(2, 'Bikash', 'Kafle', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4), 'Female',
                            'BSc. Ethical Hacking'),
                           (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8), 'Female',
                            'BSc. Ethical Hacking'),
                           (1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing')]
        self.assertEqual(array_to_sort, expected_result)

    def test_search(self):
        user.radio_ascending.invoke()
        user.combo_sort.set('Id')
        array_containing_data = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                                  'BSc. Computing'),
                                 (2, 'Aayusha', 'Upreti', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4),
                                  'Female', 'BSc. Ethical Hacking'),
                                 (3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8),
                                  'Female', 'BSc. Ethical Hacking'),
                                 (4, 'Manoj', 'Baniya', '9801254686', 'Chobar', datetime.date(1993, 9, 11), 'Male',
                                  'Civil Engineering'),
                                 (5, 'Prabin', 'Regmi', '9842512132', 'Bangalore', datetime.date(1997, 5, 4), 'Male',
                                  'Civil Engineering'),
                                 (6, 'Bikash', 'Lama', '9854210234', 'Harion', datetime.date(1999, 9, 2), 'Male',
                                  'BSc. Computing'),
                                 (7, 'Udaya', 'Shrestha', '9851206548', 'Balganga', datetime.date(2001, 7, 2), 'Male',
                                  'Commerce'),
                                 (8, 'Sabina', 'Gautam', '9804587658', 'Gaushala', datetime.date(1997, 4, 10), 'Female',
                                  'BSc. Computing'),
                                 (9, 'Dinesh', 'Karki', '9808876132', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                                  'Commerce')]
        # Searching through ID
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 4)
        user.combo_search.set('Id')
        final = user.search(array_containing_data)
        expected_result = [(4, 'Manoj', 'Baniya', '9801254686', 'Chobar', datetime.date(1993, 9, 11), 'Male',
                            'Civil Engineering')]
        self.assertEqual(final, expected_result)

        # Searching through Last Name
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'upreti')
        user.combo_search.set('Last Name')
        final = user.search(array_containing_data)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (2, 'Aayusha', 'Upreti', '9814561321', 'Bhaktapur', datetime.date(2004, 5, 4),
                            'Female', 'BSc. Ethical Hacking')]
        self.assertEqual(final, expected_result)

        # Searching through First Name
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'prabin')
        user.combo_search.set('First Name')
        final = user.search(array_containing_data)
        expected_result = [(5, 'Prabin', 'Regmi', '9842512132', 'Bangalore', datetime.date(1997, 5, 4), 'Male',
                            'Civil Engineering')]
        self.assertEqual(final, expected_result)

        # Searching through ID
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, '')
        user.combo_search.set('Id')
        final = user.search(array_containing_data)
        expected_result = None
        self.assertEqual(final, expected_result)

        # Searching through Contact
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, '9851206548')
        user.combo_search.set('Contact')
        final = user.search(array_containing_data)
        expected_result = [(7, 'Udaya', 'Shrestha', '9851206548', 'Balganga', datetime.date(2001, 7, 2), 'Male',
                            'Commerce')]
        self.assertEqual(final, expected_result)

        # Searching through Gender
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Male')
        user.combo_search.set('Gender')
        final = user.search(array_containing_data)
        expected_result = [(1, 'Aayush', 'Upreti', '9812365486', 'Thimi', datetime.date(2002, 11, 2), 'Male',
                            'BSc. Computing'),
                           (4, 'Manoj', 'Baniya', '9801254686', 'Chobar', datetime.date(1993, 9, 11), 'Male',
                            'Civil Engineering'),
                           (5, 'Prabin', 'Regmi', '9842512132', 'Bangalore', datetime.date(1997, 5, 4), 'Male',
                            'Civil Engineering'),
                           (6, 'Bikash', 'Lama', '9854210234', 'Harion', datetime.date(1999, 9, 2), 'Male',
                            'BSc. Computing'),
                           (7, 'Udaya', 'Shrestha', '9851206548', 'Balganga', datetime.date(2001, 7, 2), 'Male',
                            'Commerce'),
                           (9, 'Dinesh', 'Karki', '9808876132', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                            'Commerce')]
        self.assertEqual(final, expected_result)

        # Searching through Degree
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, 'Commerce')
        user.combo_search.set('Degree')
        final = user.search(array_containing_data)
        expected_result = [(7, 'Udaya', 'Shrestha', '9851206548', 'Balganga', datetime.date(2001, 7, 2), 'Male',
                            'Commerce'),
                           (9, 'Dinesh', 'Karki', '9808876132', 'Balaju', datetime.date(1999, 10, 7), 'Male',
                            'Commerce')]
        self.assertEqual(final, expected_result)

        # Searching through Date of birth
        user.entry_search.delete(0, END)
        user.entry_search.insert(0, f'{datetime.date(1998, 10, 8)}')
        user.combo_search.set('Date of Birth')
        final = user.search(array_containing_data)
        expected_result = [(3, 'Amrita', 'Lamichanne', '9805166525', 'Pepsicola', datetime.date(1998, 10, 8),
                            'Female', 'BSc. Ethical Hacking')]
        self.assertEqual(final, expected_result)

    def test_clear(self):
        user.entry_id.insert(0, 15665)
        user.entry_f_name.insert(0, 'manish')
        user.entry_l_name.insert(0, 'rai')
        user.entry_address.insert(0, 'Nowhere')
        user.entry_contact.insert(0, '5646548951')
        user.radio_custom.invoke()
        user.combo_degree.set('Commerce')
        user.combo_day.set(5)
        user.combo_month.set(11)
        user.combo_year.set(2015)

        user.clear()

        self.assertEqual(user.entry_id.get(), '')
        self.assertEqual(user.entry_f_name.get(), '')
        self.assertEqual(user.entry_l_name.get(), '')
        self.assertEqual(user.entry_address.get(), '')
        self.assertEqual(user.entry_contact.get(), '')
        self.assertEqual(user.gender.get(), 'Male')
        self.assertEqual(user.combo_degree.get(), 'BSc. Computing')
        self.assertEqual(user.combo_day.get(), str(user.dt.day))
        self.assertEqual(user.combo_month.get(), str(user.dt.month))
        self.assertEqual(user.combo_year.get(), str(user.dt.year))


if __name__ == '__main__':
    m = MainWindow()
    user = User(m.container_frame, m)
    unittest.main()

import unittest
import os
class TestPipeline(unittest.TestCase):
    def test_check_output_file(self):
        path_current_directory = os.path.dirname(os.path.abspath(__file__))

        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.abspath(os.path.join(current_dir, os.pardir))
        data_path = os.path.join(base_path, 'data')

        my_sqlite = os.path.join(data_path, 'data.sqlite')

        print(my_sqlite)

        # Check if the file exists
        self.assertTrue(os.path.isfile(my_sqlite), "data.sqlite does not exist in the data folder.")
        if os.path.isfile(my_sqlite):
            print('data.sqlite exists.')

if __name__ == '__main__':
    unittest.main(exit=False)
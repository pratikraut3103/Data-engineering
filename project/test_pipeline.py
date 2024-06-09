import unittest
import os
class TestPipeline(unittest.TestCase):
    def check_output_file(self):
        path_current_directory = os.path.dirname(os.path.abspath(__file__))
        my_sqlite = os.path.join(path_current_directory, '..', 'data', 'data.sqlite')

        # Check if the file exists
        self.assertTrue(os.path.isfile(my_sqlite), "data.sqlite does not exist in the data folder.")
        if os.path.isfile(my_sqlite):
            print('data.sqlite exists.')

if __name__ == '__main__':
    unittest.main()
import unittest
import os
import uuid
import shutil
from appdirs import user_cache_dir
from rss_reader_package.utils.count_files import count_files_by_type


class TestCountFiles(unittest.TestCase):
    def test_count_files_by_type(self):
        test_dir = os.path.join(user_cache_dir(), "Test")
        os.mkdir(test_dir)
        for i in range(5):
            with open(os.path.join(test_dir, f"{uuid.uuid4()}.txt"), "w") as temp_file:
                temp_file.write("")
        self.assertEqual(count_files_by_type(test_dir, ".txt"), 5)
        self.assertEqual(count_files_by_type(test_dir, None), 5)
        self.assertEqual(count_files_by_type(test_dir, ".html"), 0)
        for i in range(3):
            with open(os.path.join(test_dir, f"{uuid.uuid4()}.tmp"), "w") as temp_file:
                temp_file.write("")
        self.assertEqual(count_files_by_type(test_dir, ".tmp"), 3)
        self.assertEqual(count_files_by_type(test_dir, None), 8)
        self.assertEqual(count_files_by_type(test_dir, ".txt"), 5)
        shutil.rmtree(test_dir)


unittest.main()

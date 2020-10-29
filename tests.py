from YaUploader import YaUploader
import unittest
from yatoken import YATOKEN  #the file yatoken.py contains variable YATOKEN with Yandex TOKEN


class TestYaUploader(unittest.TestCase):
    def setUp(self):
        self.YATOKEN = YATOKEN
        self.yadisk = YaUploader(self.YATOKEN)
        self.foldername = "testfolder"

    def tearDown(self):
        pass

    def test_YaUploader_create_folder(self):
        print(
            f"TEST: test on creation of directory {self.foldername}. Waiting 200 or 201 code")
        expected = [200, 201]
        actual = self.yadisk.create_folder(self.foldername)
        self.assertIn(actual, expected)

    def test_YaUploader_create_the_same_folder(self):
        print(
            f"TEST: AGAIN test on creation of directory {self.foldername}. Waiting 409 code")
        expected = [409]
        actual = self.yadisk.create_folder(self.foldername)
        self.assertIn(actual, expected)


if __name__ == "__main__":
    unittest.main()

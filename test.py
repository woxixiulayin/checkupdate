import unittest
from check_update import *
from config import config_test

class Testcheck(unittest.TestCase):

    # def test_shellcmd(self):
    #     cmd = ['ls', '.']
    #     self.assertTrue(isinstance(shellCmd(cmd), tuple))

    # def test_gitfetch(self):
    #     result = gitfetch_cmd(config_test)
    #     self.assertEqual(result[0], 0)

    def test_checkup(self):
        result = check_update(config_test)
        self.assertTrue(isinstance(result[0], int))
        self.assertTrue(isinstance(result[1], bool))
        self.assertTrue(isinstance(result[2], str))
if __name__ == '__main__':
    uniitest.main()

import unittest
import NetEaseMusic


class Test_xMusicWeb(unittest.TestCase):
    def test_qq(self):
        l = NetEaseMusic.qq.getList('https://y.qq.com/n/yqq/playlist/3363492195.html')
        self.assertGreater(len(l), 0)

    def test_163(self):
        l = NetEaseMusic._163.getList('http://music.163.com/#/playlist?id=98176052')
        self.assertGreater(len(l), 0)

if __name__ == '__main__':
    unittest.main()

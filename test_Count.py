#-*- coding: utf-8 -*-

import unittest
import os
import time
from HTMLTestRunnerTest import HTMLTestRunner

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'F0O')
        self.assertEqual('foo'.upper(), 'F0O')


    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    print('All case number')
    print(test_result.testsRun)
    print('Failed case number')
    print(len(test_result.failures))
    print('Failed case and reason')
    print(test_result.failures)
    for case, reason in test_result.failures:
        print case.id()
        print reason

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    reportpath = os.path.join(os.getcwd(), 'ReportTest')
    print reportpath
    if not os.path.exists(reportpath):
        os.mkdir(reportpath)
    filename = os.path.join(reportpath, now + "_result.html")
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'ReportTest',
        description=u'用例执行情况:',
        verbosity=2, retry=0, save_last_try=True)
    # verbosity表示报告级别
    # retry表示失败重试机制
    runner.run(suite)
    fp.close()



if __name__ == '__main__':
    main()
# how to run

cd ./RunUnittest

python test_Count.py

# show

```angular2html
Ran 3 tests in 0.000s

FAILED (failures=1)
All case number
3
Failed case number
1
Failed case and reason
[(<__main__.TestStringMethods testMethod=test_upper>, 'Traceback (most recent call last):\n  File "test_Count.py", line 11, in test_upper\n    self.assertEqual(\'foo\'.upper(), \'F0O\')\nAssertionError: \'FOO\' != \'F0O\'\n')]
__main__.TestStringMethods.test_upper
Traceback (most recent call last):
  File "test_Count.py", line 11, in test_upper
    self.assertEqual('foo'.upper(), 'F0O')
AssertionError: 'FOO' != 'F0O'

/Users/xinxi/PycharmProjects/RunUnittest/ReportTest
ok test_isupper (__main__.TestStringMethods)
ok test_split (__main__.TestStringMethods)
F  test_upper (__main__.TestStringMethods)

Time Elapsed: 0:00:00.000318
```
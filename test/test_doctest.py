import unittest
import doctest
import pk3hunum

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pk3hunum))
    return tests

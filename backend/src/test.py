from unittest import TestLoader, TextTestRunner, TestSuite
from database import MongoTest


def test_all():

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MongoTest)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

test_all()

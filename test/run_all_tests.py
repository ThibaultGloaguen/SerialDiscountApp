import unittest
import sys
from test.integration_test.route_test import TestRoute

if __name__ == '__main__':

    integration = unittest.TestLoader().loadTestsFromTestCase(TestRoute)
    all_tests = unittest.TestSuite([integration])
    result = unittest.TextTestRunner(verbosity=2).run(all_tests)
    if result.wasSuccessful():
        sys.exit(0)
    sys.exit(-1)

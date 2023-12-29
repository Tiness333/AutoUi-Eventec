import unittest
# from HTMLTestRunner import HTMLTestRunner



suite = unittest.TestSuite()
tests = ["Testcase.testcase.Auto_Test.test_case001","Testcase.testcase.Auto_Test.test_case002"]
suite.addTest(unittest.TestLoader().loadTestsFromNames(tests))
unittest.TextTestRunner().run(suite)

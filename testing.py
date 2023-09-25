# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# #
# # class PythonOrgSearch(unittest.TestCase):
# #
# #     def setUp(self):
# #         self.driver = webdriver.Edge()
# #
# #     def test_search_in_python_org(self):
# #         driver = self.driver
# #         driver.get("http://www.python.org")
# #         self.assertIn("Python", driver.title)
# #         elem = driver.find_element(By.NAME, "q")
# #         elem.send_keys("pycon")
# #         elem.send_keys(Keys.RETURN)
# #         self.assertNotIn("No results found.", driver.page_source)
# #
# #
# #     def tearDown(self):
# #         self.driver.close()
# #
# # if __name__ == "__main__":
# #     unittest.main()

# import pytest
#
#
# def f():
#     raise SystemExit(2)
#
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert "e" in x
# class TestClassDemoInstance:
#     value = 0
#
#     def test_one(self):
#         self.value = 1
#         assert self.value == 1
#
#     def test_two(self):
#         assert self.value == 1

# class TestClass:
#     value=0
#
#     def test_one(self):
#         self.value=1
#         assert self.value==1
#
#     def test_two(self):
#         self.value=1
#         assert self.value==1

# import pytest
# import sys
#
#
# class MyPlugin:
#     def pytest_sessionfinish(self):
#         print("*** test run reporting finishing")
#
#
# if __name__ == "__main__":
#     sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
import pytest


@pytest.mark.parametrize("input, expected" ,[
    ( [1, 2, 3, 4], 4),
    ( [7, 8, 9 , 10], 10)
])
def test_max(input, expected):
    "Verify the max function works"
    Output = max(input)
    assert Output == expected



@pytest.mark.parametrize("input, expected" ,[
    ( [1, 2, 3, 4], 1),
    ( [7, 8, 9 , 10], 7)
])
def test_min(input, expected):
    "Verify the min function works"
    Output = min(input)
    assert Output == expected










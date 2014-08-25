"""
Functional Tests


"""

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Kenneth has heard about a cool new site
        # He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices that the title of the page mentioned 'To-Do'
        self.assertIn('To-Do', self.browser.title)

        self.fail('Finish the test')

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main(warnings='ignore')

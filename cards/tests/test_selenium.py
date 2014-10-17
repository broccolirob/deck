from time import sleep
from django.core.urlresolvers import reverse
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from django.test import LiveServerTestCase
from cards.models import Player


class SeleniumTests(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def admin_login(self):
        Player.objects.create_superuser('admin', 'admin@example.com', 'admin')
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
        self.selenium.find_element_by_name('username').send_keys('admin')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('admin')
        password_input.send_keys(Keys.RETURN)
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

    def test_admin_create_card(self):
        self.admin_login()
        self.selenium.find_elements_by_link_text('Cards')[1].click()
        self.selenium.find_element_by_link_text('Add card').click()
        self.selenium.find_element_by_name('rank').send_keys('ace')
        suit_dropdown = self.selenium.find_element_by_name('suit')
        for option in suit_dropdown.find_elements_by_tag_name('option'):
            if option.text == 'heart':
                option.click()
        self.selenium.find_element_by_css_selector('input[value="Save"]').click()
        sleep(.1)
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('The card "ace of 3" was added successfully', body.text)

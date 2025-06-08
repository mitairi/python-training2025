from selenium.webdriver.common.by import By

class ContactHelper:

    def __init__(self, app):
        self.app = app
        
    def open_new_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contacts_page()
        self.fill_in_contact_info(contact)
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()     

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH , "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.XPATH , "//img[@alt='Edit']").click()
        self.fill_in_contact_info(contact)
        wd.find_element(By.NAME, "update").click()    
        self.return_to_home_page()

    def fill_in_contact_info(self, contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)     

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

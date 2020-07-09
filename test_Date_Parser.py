#This will validate date field

from selenium import webdriver
import pytest
from DateParser.DatePage import DatePage
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
driver.get("https://vast-dawn-73245.herokuapp.com/")
driver.maximize_window()
class Testdateparser():
    def test_dateparsercheck(self,getData):
        date = driver.find_element_by_class_name("form-control") #Locate the date field
        date.clear()
        date.send_keys(getData["Date_format"])
        driver.find_element_by_class_name("btn-default").click()
        result = driver.find_element_by_xpath("(.//*[@class='col-md-6'])[2]").text #Capture the expected Result
        if getData["Expected_Result"] in result:
            print(getData["Date_format"] + "    PASS")
        else:
            print(getData["Date_format"] + "    FAIL")

#Get the test data from DatePage.py

    @pytest.fixture(params=DatePage.test_data)
    def getData(self, request):
        return request.param



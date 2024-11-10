strng = "jiosjxaoijirepedmo;iepdeo8943uhe37"
vwlstr = [x for x in strng if x in 'aeiou']
vwlstr.sort(reverse=False)
print(''.join(vwlstr))

import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
    
    
def reverse_string(s):
    return s[::-1]

# Example usage:
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)  # Output: !dlroW ,olleH

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the web page
    driver.get("http://example.com")

    # Trigger the alert
    driver.find_element(By.ID, "trigger-alert").click()

    # Switch to the alert
    alert = driver.switch_to.alert

    # Accept the alert (click OK)
    alert.accept()

    # If you need to dismiss the alert (click Cancel)
    # alert.dismiss()

finally:
    # Close the browser
    driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the web page
    driver.get("http://example.com")

    # Click on the link that opens a new window
    driver.find_element(By.ID, "open-new-window").click()

    # Get the current window handle
    main_window = driver.current_window_handle

    # Get all window handles
    all_windows = driver.window_handles

    # Switch to the new window
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # Perform actions in the new window
    new_window_content = driver.find_element(By.TAG_NAME, 'body').text
    print(new_window_content)

    # Close the new window and switch back to the main window
    driver.close()
    driver.switch_to.window(main_window)

finally:
    # Close the browser
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the web page
    driver.get("http://example.com")

    # Find all the links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    # Print the text and href of each link
    for link in links:
        link_text = link.text
        link_url = link.get_attribute("href")
        print(f"Text: {link_text}, URL: {link_url}")

finally:
    # Close the browser
    driver.quit()

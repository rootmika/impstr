import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up the WebDriver (Chrome in this example)
driver_path = r"C:\Users\UTSUKIRA\Downloads\impstr\chromedriver.exe"
chrm_option = Options()
chrm_option.add_argument('--headless=new')
driver = webdriver.Chrome(service=Service(driver_path),options = chrm_option)
# driver = webdriver.Chrome()  # Make sure you have the ChromeDriver in your PATH or specify its path
# driver.maximize_window()

try:
    # Navigate to the target URL
    # print(0)
    driver.get("https://forms.office.com/r/xkK7y3afMX")
    # time.sleep(3)  # Wait 5 seconds after loading the page

    # Part 1: Click on the element with class '.css-130'
    # print(1)
    # script_part1 = """
    # var interval = setInterval(function() {
    # var x = document.querySelector('.css-130');
    # if (x) {
    #     x.click();
    #     clearInterval(interval); // Stop checking once clicked
    # }
    # }, 100); // Check every 100 milliseconds

    # """
    # driver.execute_script(script_part1)
    # driver.execute_script("console.log('siji');var x = document.querySelector('.css-107');x.click()")
    driver.execute_script("div1 = Array.from(document.querySelectorAll('button, a')).find(el => el.textContent.trim() === 'Start now');div1.click()")
    
    # time.sleep(3)  # Wait 5 seconds before the next step

    # Part 2: Set the value of the input field to 'Impostor'
    # print(2)
    # script_part2 = """
    # var inputField = document.querySelector('input[placeholder="Enter your answer"]');
    # inputField.value = 'Impostor';
    # """
    # driver.execute_script(script_part2)

    
    # # Wait for the input field and paste "Impostor" into the input with class "-at-225"
    input_field = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your answer"]')
    input_field.send_keys('Impostor')
    # time.sleep(3)
    # print("step 1")
    # time.sleep(2)  # Wait 5 seconds before the next step

    # Part 3: Click on the element with class '.css-239'
    # print(3)
    # script_part3 = "var y = document.querySelector('.css-239');y.click();"
    # driver.execute_script(script_part3)
    driver.execute_script("var button = Array.from(document.querySelectorAll('button, a')).find(el => el.textContent.trim() === 'Submit');button.click()")
    # time.sleep(1)
    print("Success")
except:
    print("Fail")


finally:
    # Close the browser after completing the task
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class trains():
    def __init__(self,src,dest,date):
        self.driver = webdriver.Chrome()

        self.src=src
        self.dest=dest
        self.date=date


    # Navigate to site
        self.url=self.driver.get(f"https://www.ixigo.com/search/result/train/{src}/{dest}/{date}//1/0/0/0/ALL")
        return self.url

    def fair(self):
        # Initialize Selenium WebDriver
        driver = webdriver.Chrome()
        
        # Load the webpage
        driver.get(self.url)
        time.sleep(3)  # Wait for the page to load

        # Extract data (Assuming the website has flights listed in some specific tags like <div> or <span>)
        info= driver.find_elements(By.CSS_SELECTOR, "train-data-wrapper")  # Change selector according to website structure
        print(f"{len(info)}Item found")
        print(info.get_attribute("outerHTML"))
        time.sleep(3)
        
        # Process and print the Trains data
        self.train_data = []
        for data in info:
            # Modify selectors based on the website's structure
            price = data.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div[3]/div[2]/ul/li[2]/div/div/div[2]/div[3]/div[1]/div[1]/span[2]/div/span[2]").text
            destination = data.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div[3]/div[2]/ul/li[2]/div/div/div[1]/div[2]/div/a/div/div[3]/div[2]").text
            departure = data.find_element(By.XPATH, "//*[@id='content']/div/div[2]/div[3]/div[2]/ul/li[2]/div/div/div[1]/div[2]/div/a/div/div[1]/div[2]").text
            name = data.find_element(By.CSS_SELECTOR, "train-name").text
            
            self.train_data.append({
                'Name':name,
                'price': price,
                'destination': destination,
                'departure': departure
            })
        
        driver.quit()
        for data in self.train_data:
            print(f"Name:{data['Name']},Price: {data['price']}, Destination: {data['destination']}, Departure: {data['departure']}")
        

# URL of the website to scrape (adjust this based on your target)
source=input("Input the code of source railaway station")
destination=input("Input the code of destination railaway station")
date=int(input("Input the date you have to travel in [DDMMYYYY]"))

train = trains(source,destination,date)

# Display scraped data




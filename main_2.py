from selenium import webdriver  # Import the webdriver module from selenium for controlling the web browser
from selenium.webdriver.common.by import By  # Import By to locate elements on a webpage
from selenium.webdriver.support.ui import WebDriverWait  # Import WebDriverWait to wait for certain conditions
from selenium.webdriver.support import \
    expected_conditions as EC  # Import expected_conditions for various wait conditions
from selenium.webdriver.common.keys import Keys  # Import Keys to send keyboard actions
from selenium.common.exceptions import TimeoutException  # Import TimeoutException to handle timeout exceptions
import time  # Import time for adding delays in execution

# Set promised internet speeds
PROMISED_DOWN = 100  # Promised download speed
PROMISED_UP = 35  # Promised upload speed


# Define a class for the Twitter bot
class InternetSpeedTwitterBot:
    def __init__(self, twitter_handle):
        chrome_options = webdriver.ChromeOptions()  # Create an object for Chrome options
        chrome_options.add_experimental_option('detach', True)  # Option to keep the browser open after script completes
        self.driver = webdriver.Chrome(options=chrome_options)  # Initialize Chrome browser with options
        self.down = None  # Initialize variable to store download speed
        self.up = None  # Initialize variable to store upload speed
        self.twitter_handle = twitter_handle  # Store the Twitter handle of the service provider

    # Method to get internet speed
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")  # Open Speedtest website
        time.sleep(5)  # Wait for the page to load

        # Click on the 'Go' button to start the speed test
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")  # Locate the 'Go' button
        go_button.click()  # Click the 'Go' button

        # Wait for the speed test to finish
        time.sleep(60)  # Wait for the speed test to complete

        # Get the download and upload speeds
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text  # Get download speed
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text  # Get upload speed

    # Method to tweet at the internet service provider
    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN or float(self.up) < PROMISED_UP:
            # If the internet speed is below the promised speeds, tweet a complaint
            self.driver.get("https://x.com/login")  # Open Twitter login page

            # Wait for the sign-in element to be clickable and click it
            sign_in_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))
            )
            sign_in_element.click()  # Click the sign-in element

            # Wait for the username field, then enter username
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_field.send_keys("YOUR EMAIL", Keys.RETURN)  # Enter email and press return

            try:
                # Wait for the password field and enter password
                password_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("TWITTER PASSWORD", Keys.RETURN)  # Enter password and press return

            except TimeoutException:
                # If password field is not found, handle alternative login flow
                username_field_2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
                )
                username_field_2.send_keys('USERNAME', Keys.RETURN)  # Enter username and press return

                password_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("TWITTER PASSWORD", Keys.RETURN)  # Enter password and press return

                time.sleep(5)  # Wait for a while

            # Wait for the tweet box to be present
            tweet_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']"))
            )

            # Type the tweet and post it
            tweet_box.send_keys(f"@{self.twitter_handle} My internet speed is too slow, here is what I'm getting "
                                f"Download Speed: {self.down}Mbps, Upload Speed: {self.up}Mbps. Which isn't "
                                f"your guaranteed speed")
            tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)  # Send the tweet

        else:
            # If the internet speed is as promised, tweet a compliment
            self.driver.get("https://x.com/login")  # Open Twitter login page

            # Wait for the sign-in element to be clickable and click it
            sign_in_element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Sign in')]"))
            )
            sign_in_element.click()  # Click the sign-in element

            # Wait for the username field, then enter username
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "text"))
            )
            username_field.send_keys("YOUR EMAIL", Keys.RETURN)  # Enter email and press return

            try:
                # Wait for the password field and enter password
                password_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("TWITTER PASSWORD", Keys.RETURN)  # Enter password and press return

            except TimeoutException:
                # If password field is not found, handle alternative login flow
                username_field_2 = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 'input[data-testid="ocfEnterTextTextInput"]'))
                )
                username_field_2.send_keys('USERNAME', Keys.RETURN)  # Enter username and press return

                password_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "password"))
                )
                password_field.send_keys("TWITTER PASSWORD", Keys.RETURN)  # Enter password and press return

                time.sleep(5)  # Wait for a while

            # Wait for the tweet box to be present
            tweet_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']"))
            )

            # Type the tweet and post it
            tweet_box.send_keys(f"@{self.twitter_handle} My internet speed is excellent today! "
                                f"Download Speed: {self.down}Mbps, Upload Speed: {self.up}Mbps. Keep up the good work!")
            tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)  # Send the tweet


# Initialize the object and call the methods
bot = InternetSpeedTwitterBot(
    "SERVICE PROVIDER")  # Create an instance of the bot with the Twitter handle of the service provider
bot.get_internet_speed()  # Get the internet speed
print(f"Download Speed: {bot.down}Mbps")  # Print the download speed
print(f"Upload Speed: {bot.up}Mbps")  # Print the upload speed
bot.tweet_at_provider()  # Tweet at the service provider based on the internet speed

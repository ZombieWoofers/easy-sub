from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

#options = Options()
#options.add_argument("--headless")
#driver = webdriver.Firefox(firefox_options=options, executable_path="")
#print("Firefox Headless Browser Invoked")

driver = webdriver.Firefox()
print("Checking for sub jobs, please stand by")
driver.get("https://sfusd.eschoolsolutions.com/logOnInitAction.do")
#assert "Python" in driver.title
id = driver.find_element_by_name("userID")
pin = driver.find_element_by_name("userPin")
id.clear()
pin.clear()
id.send_keys("")
pin.send_keys("")
submit = driver.find_element_by_name("submit")
submit.click() # look at how to override so it includes a wait
driver.implicitly_wait(2) 
jobs = driver.find_element_by_id("sidious.menu.title.AvailableJobs")
jobs.click()
# now set the date range and search, start is set to today's date

endDate = driver.find_element_by_name("endDate")
endDate.clear()
endDate.send_keys("03/02/2018")
search = driver.find_element_by_class_name("submitButton")
search.click()

# replace with polling against the 'searching' pop-up

driver.implicitly_wait(20)   #update this to wait for the results to appear based on some id/name/etc

listing = driver.find_elements_by_link_text("Details")
print("Jobs: ")
# for len(listing), get each element then?
#jobListings = driver.find_element_by_id("sidious.job.top.0")

detailTop = driver.find_elements_by_class_name("text")

for x in range(0, len(detailTop)):
	print(detailTop[x].text)
print(len(listing))

# partial link text

# 2 of these:  tr id="sidious.job.top.1"
# first one has the start time, second has the end time

# 'Details' button is : tr id="sidious.job.details.1"
# get list of td elements within the tr and get class="text"

# assert "No results found." not in driver.page_source
# driver.close()

requests.post('https://textbelt.com/text', {
  'phone': 'your_number',
  'message': 'Found x available jobs',
  'key': 'textbelt',
})
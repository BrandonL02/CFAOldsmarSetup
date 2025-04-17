# CFAOldsmarSetup

## Management Setup Generator

This program is designed to create an automated, premade setup for **CFA Oldsmar** leadership by performing the following tasks:

- Webscraping the HotSchedules website using Python's Selenium library
- Organizing the scraped data using a Pandas dataframe
- Assigning employees to positions between **2:00 PM – 10:45 PM** based on their unique schedules
- Ensuring:
  - No one is outside longer than **1 hour** taking orders on the iPad
  - No one is outside longer than **2 hours** taking Cash payments
- Displaying the results to the setup sheet for practical application in the restaurant
- Automatically terminating the program after setup is completed

---

## Program Requirements

To function correctly, the program requires the following libraries:

- python-docx: to read from and write to a word document
    - pip install python-docx
- selenium: to seamlessly scrape the hotschedules website using Google chromedriver
    - pip install -U selenium
- pandas: to organize the raw date from the site prior to creating the schedule
  - pip install pandas
---

## Example Usage

📄 **Example Setup Output**  
You can view an example of the expected setup output in this [Word Document](https://github.com/BrandonL02/CFAOldsmarSetup/blob/6774427c8a9ed58b25ee1143366c6f5617ce97bf/example_setup/CFA%20example%20setup.docx) or by checking the image below:

![Example Output](https://github.com/BrandonL02/CFAOldsmarSetup/blob/6774427c8a9ed58b25ee1143366c6f5617ce97bf/example_setup/cfa_setup_example.png)

> **Note:** All names shown in the example are **for demonstration purposes only**.

---

Feel free to reach out with any suggestions or improvements!


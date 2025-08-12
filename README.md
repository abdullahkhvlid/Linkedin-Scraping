# LinkedIn Job Scraper
This project automates the process of scraping job postings from LinkedIn using Selenium and Python. It logs into LinkedIn, performs a job search based on a specified keyword, dynamically scrolls through the job listings to load results, extracts relevant job information, and saves the data to an Excel file for further analysis or use.

Features
Automated login to LinkedIn with user credentials

Keyword-based job search on LinkedIn Jobs

Dynamic scrolling to load multiple job listings

Extraction of job title, company name, location, and posting date

Data export to Excel format for easy access and manipulation

Handles delays and loading times using explicit waits for robustness

Technologies Used
Python 3.x

Selenium WebDriver for browser automation

pandas for data handling and Excel export

Google Chrome and ChromeDriver for browser interaction

Prerequisites
Python installed on your machine

Google Chrome browser installed

ChromeDriver executable matching your Chrome version (ensure ChromeDriver is in your system PATH or specify its path in the script)

Required Python packages: selenium, pandas

You can install required packages using:
pip install selenium pandas

Usage Instructions
Set up LinkedIn credentials
Replace the placeholders "your_email_here" and "your_password_here" in the script with your actual LinkedIn login credentials.

Modify the search keyword
Change the value of the search_query variable to any job title or keyword you want to search for on LinkedIn.

Run the script
Execute the script in your Python environment. The script will:

Open a Chrome browser window

Log in to LinkedIn

Navigate to the job search page with the specified keyword

Scroll the job listings until at least 25 jobs are loaded or a maximum number of scroll attempts is reached

Extract job title, company name, location, and date posted for each job

Save the extracted data to linkedin_jobs_25.xlsx

View results
Open the generated Excel file to see the scraped job data.

How It Works
The script initializes Chrome with options to disable notifications.

It navigates to the LinkedIn login page and inputs the provided credentials.

After logging in, it opens the LinkedIn job search URL filtered by the keyword.

The job listings container is located and scrolled programmatically using JavaScript to trigger dynamic loading of additional job cards.

The script collects details for each job card by locating elements corresponding to title, company, location, and date posted.

Data is stored in a list of dictionaries, converted to a pandas DataFrame, and exported as an Excel file.

Finally, the browser session is closed cleanly.

Important Notes
LinkedIn actively monitors and restricts automated scraping. Use this script responsibly and in accordance with LinkedIn's terms of service.

To avoid detection, consider adding randomized delays or running the script at a moderate frequency.

This script assumes a stable LinkedIn page structure. If LinkedIn updates its HTML/CSS, selectors may need to be updated accordingly.

Ensure your ChromeDriver version matches your installed Chrome browser version to prevent compatibility issues.

The script currently scrapes a maximum of 25 job listings per run. You can adjust the max_scroll_attempts or logic to scrape more if needed.

Troubleshooting
If the script fails to find elements, it might be due to changes in LinkedIn’s UI or slow page loading. Adjust explicit wait times or verify the selectors.

For ChromeDriver issues, download the latest compatible version from ChromeDriver - WebDriver for Chrome.

If login fails, verify credentials and consider enabling two-factor authentication app passwords if applicable.

Future Improvements
Add functionality to scrape additional job details such as job description, salary estimates, and applicant counts.

Implement headless browser operation for running without a visible window.

Add command-line arguments to customize search queries and output filenames.

Integrate proxies or VPN rotation to reduce the risk of IP blocking.

Export data to other formats such as CSV or JSON.

License
This project is provided for educational purposes only. Use responsibly and respect website terms of service.


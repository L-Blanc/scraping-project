#Florida Public School Scraper

For this project, I used a combination of the Selenium and BeautifulSoup python libraries to scrape school information (school name, school distrct/city, total student count, student to teacher ratio, and overall Niche grade) from public K-12 schools in Florida from Niche.com

page url(https://www.niche.com/k12/search/best-public-schools/s/florida/).

Niche provides report cards for K-12 schools and attributes ratings to schools based on a series of factors. You can find out more about about their methodology here:https://www.niche.com/k12/rankings/methodology/  school rankings

- First, I used the variable csvfile to open a csv file named "schools.csv" to collect the information I would be scraping from the page.
To that csv, I used the writerow function to create a row for each item I would be scraping.

- Next, I created a for loop to click a button and iterate over each of the 153 pages related to my search results.

- Then, inside of that for loop, I collected all of  the divs off of the page that had the class "search result" in the variable "list_of_schools" so that I would ONLY collect the school results related to my filtered search ("public school", "Florida") and not pick up any of the divs containing the sponsored results throughout the page.

- Next, I created a function (scrape_one_school()) to scrape the information for one school and put a for loop in that function iterates over items in the list created by the variable list_of_schools.

- Within the function scrape_one_school,  I created a list (school_details) that returns the information I scraped from each div into a list.

- Those list items are then written in order into each row of the csv file schools.csv

- To ensure the items are being collected, I created another for loop that iterates over the list (school_details) and prints each schools information in the terminal.

The most difficulty I had was chosing a comfortable sleep time that would let me bypass bot captchas.

I also had difficulty figuring out how to embedd my scraping for loop into my button clicking for loop so that the scrape_one_school() function would run on each page.

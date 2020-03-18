# Florida Public School Scraper

For this project, I used a combination of the Selenium and BeautifulSoup python libraries to scrape school information (school name, school distrct/city, total student count, student to teacher ratio, and overall Niche grade) from public K-12 schools in Florida from Niche.com

page url(https://www.niche.com/k12/search/best-public-schools/s/florida/).

Niche provides report cards for K-12 schools and attributes ratings to schools based on a series of factors. You can find out more about about their methodology here:https://www.niche.com/k12/rankings/methodology/  

## Step 1: Create a csv file for the scrapped results to be written to
- First, I used the variable csvfile to open a csv file named "schools.csv" to collect the information I would be scraping from the page and created a python object "c" to manipulate.
To that csv, I used the c.writerow() function to create a row heading for each item I would be scraping.

#Step 2: Use BeautifulSoup to collect the search results on the page
- Next, I used the variable ("page") to launch my page url and created my soup variable to collect all of the divs off the page that had the class "search result" into the variable ("list_of_schools") so that I would ONLY collect the school results related to my filtered search for "public schools in Florida" and not pick up any of the divs containing the sponsored results throughout the page.

## Step 3: Create a function to scrape the school information
-  Next, I created a function (scrape_one_school()) that uses the find() function to target different text elements within the scraped divs and stores that information into individual variables(school_names, district_or_city, student_count, niche_grade)
  - scrape_one_school() scrapes the information for one school and uses a for loop to iterate over each school (div) in the list of divs created by the variable "list_of_schools".

- Within the function scrape_one_school(), the list (school_details) returns the information I scraped from each div into a list.

- Those list items are then written in order into each row of the csv file schools.csv using c.writerow()

- To ensure the items are being collected, I created another for loop within the function that iterates over the list (school_details) and prints each schools bit of information in the terminal.

## Step 4: Use Selenium to click a button and scrape the next page of your results
- I then created the scrape() function where I call the function scrape_one_school() and pass the soup variable to scrape the schools on the first page being launched page.
- Then I use the Selenium library to create a clicker that uses .click() to click the 'next' button on the bottom of the page.

- Inside this scrape() function I use a for loop to iterate the scrape_one_school() function over each of the 153 pages that are being clicked to related to my search results for public schools in Florida.


Basically I am telling the scraper:
  1. Open the url
  2. Scrape all of the divs (search results) on the page and put them into a list (list_of_schools)
  3. Scrape the information from those divs using the scrape_one_school() function, write the contents (school_details) to the csvfile
  4. Call the scrape(soup) function to do this to every page of search results.
  5. Go to the next page, repeat


The most difficulty I had was chosing a comfortable sleep time that would let me bypass bot captchas.

I also had difficulty figuring out how to embedd my scrape_one_school() function into the outer for loop for my button clicking so that the scrape_one_school() function would run on each page.

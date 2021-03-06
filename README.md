# DigiKala Crawler

This is a django app for scraping data from specified digikala search urls.

**Install dependencies:**

`pip install -r requirements.txt`

**Make migrations:**

`python manage.py makemigrations`

**Migrate:**

`python manage.py migrate`

**Run project:**

`python manage.py runserver`

# API Guide

**You can use </api/doc> for swagger documentation**

 - **URL**

	 <http://localhost:8000/api/category/>


-   **Method**

    <_The request type_>

	`POST`


- **Data Params**

	- requierd 
	  digikala search url such as:

			`category=https://www.digikala.com/search/?q=%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C`


	-	optional:

		amount of pages that you want to crawl:

		`pages=15`

		(default is 5)

Features to improve project:

- Tests for api,data and models validations

- Crawl products based on availability of packs

- Automize crawl based on categories 

- more specific models

- Crawl all of the ratings and comments for better view of product

# eBay Scraper


eBay Scraper is a Python application built with Scrapy to extract product information from eBay product pages.
## Features

- Extracts product details such as title, photo URL, product URL, price, seller, and shipping price.
- Outputs the scraped data in JSON format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/ebay-scraper.git
   cd ebay-scraper


2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Usage
To run the scraper, execute the following command:

    ```bash
   scrapy crawl ebay -o output.json
 This command starts the scraper, crawls the specified eBay product page, and saves the scraped data into output.json.

4. Example 
    ```bash
   [
   {"product_data": {"title": "Size 9.5 - Jordan 4 Retro Mid Red Cement", "photo_url": "https://i.ebayimg.com/images/g/0VUAAOSwDZJmeiXy/s-l1600.jpg", "product_url": "https://www.ebay.com/itm/375503920468", "price": "US $170.00", "seller": "jocald4066", "shipping_price": "Does not ship to Ukraine"}}
   ]

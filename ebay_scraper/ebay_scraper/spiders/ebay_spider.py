import scrapy


class EbaySpider(scrapy.Spider):
    """
    Scrapy Spider for Scraping Product Data from eBay

    This spider crawls eBay product pages to extract specific data fields such as title, photo URL, price, seller information,
    and shipping details.

    Attributes:
        name (str): The name of the spider, used when running Scrapy commands.
        allowed_domains (list): List of domains spider is allowed to crawl.

    Usage:
        To run this spider, execute the following command in the terminal:
            scrapy crawl ebay -o output.json

    Fields Extracted:
        - title (str): The title of the product. Extracted from <div class="vim x-item-title">.
        - photo_url (str): URL of the main product photo. Extracted from <img data-zoom-src>.
        - product_url (str): URL of the current product page being scraped.
        - price (str): Price of the product. Extracted from <div class="x-price-primary">.
        - seller (str): Seller name. Extracted from <div class="x-sellercard-atf__info__about-seller">.
        - shipping_price (str): Shipping cost details. Extracted from <div class="ux-labels-values__values-content"> for shipping details.

    Notes:
        - Ensure the CSS selectors (used in response.css()) are updated if eBay's HTML structure changes.
        - The spider starts with a predefined URL and uses parse() method to extract and yield product_data dictionary.

    Example:
        Assume the spider starts at 'https://www.ebay.com/itm/375503920468' and retrieves product details such as title,
        photo URL, price, seller info, and shipping cost.

        For best results, run this spider in a virtual environment with Scrapy installed.
    """

    name = 'ebay'
    allowed_domains = ['ebay.com']

    def start_requests(self):
        """
        Initializes the start URL for the spider.

        Yields:
            scrapy.Request: A scrapy request object to start scraping.
        """
        url = 'https://www.ebay.com/itm/375503920468'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parses the eBay product page and extracts product data.

        Args:
            response (scrapy.http.Response): The response object containing the page source.

        Yields:
            dict: A dictionary containing product data.
        """
        product_data = {}

        # Extracting title of the product
        title = response.css('div.vim.x-item-title h1.x-item-title__mainTitle span.ux-textspans.ux-textspans--BOLD::text').get()
        product_data['title'] = title.strip() if title else None

        # Extracting photo URL of the product
        photo_url = response.css('img[data-zoom-src]::attr(data-zoom-src)').get()
        product_data['photo_url'] = photo_url if photo_url else None

        # Setting product URL
        product_data['product_url'] = response.url

        # Extracting price of the product
        price = response.css('div.x-price-primary span.ux-textspans::text').get()
        product_data['price'] = price.strip() if price else None

        # Extracting seller information
        seller = response.css('div.x-sellercard-atf__info__about-seller a.ux-action span.ux-textspans.ux-textspans--BOLD::text').get()
        product_data['seller'] = seller.strip() if seller else None

        # Extracting shipping price
        shipping_price = response.css('div.ux-labels-values__values-content span.ux-textspans.ux-textspans--BOLD.ux-textspans--NEGATIVE::text').get()
        product_data['shipping_price'] = shipping_price.strip() if shipping_price else 'Free Shipping'

        yield {
            'product_data': product_data
        }

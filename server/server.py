import os
from operator import truediv
from bs4 import BeautifulSoup
import requests
import time
import traceback
import random
from requests_html import HTMLSession
from readPages import read_page
import json
import traceback
import logging


session = HTMLSession()
dirname = os.path.dirname(__file__)

shop_name = "BeformisOverlay"

URL = "https://www.etsy.com/shop/" + shop_name + "/sold"
URL_paginated = URL + "?ref=pagination&page="
page_count = 0
products = []


def count_sell_count(product_title):
    global products
    try:
        for i in products:
            if product_title == products[i]['name']:
                return products[i]['sold'] + 1
        return 1
    except Exception as e:
        return 1


def get_product_list(soup):
    results = soup.find(class_="responsive-listing-grid")
    return results.find_all("div", class_="js-merch-stash-check-listing")


def get_page_count(soup):
    page_nav = soup.find(class_="clearfix")
    page_list = page_nav.find_all(
        "li", class_="btn btn-list-item btn-secondary btn-group-item-md hide-xs hide-sm hide-md")
    for page in page_list:
        if page == page_list[-1]:
            return page.find_all("span")[-1].get_text().strip()


def scrape_sold_product(product_element):
    product_title = product_element.find(
        "h3", class_="wt-text-caption").text.strip()
    product_link = product_element.find("a", class_="listing-link")["href"]
    product_img = product_element.find(
        'div', class_="v2-listing-card__img").find('img')['src']
    product_sold = count_sell_count(product_title)
    return {
        'name': product_title,
        'link': product_link,
        'image': product_img,
        'sold': product_sold
    }


def add_products_to_json(product_list):
    global products
    for sold_product in product_list:
        product_json = scrape_sold_product(sold_product)
        if (len(products) > 0):
            if (is_product_in_list(product_json) == False):
                products.append(product_json)
            else:
                for product in products:
                    if product['name'] == product_json['name']:
                        product['sold'] = product['sold'] + 1
        else:
            products.append(product_json)


def is_product_in_list(product_json):
    global products
    for product in products:
        if product['name'] == product_json['name']:
            return True
    return False


def write_to_file(path, data):
    products_json = json.dumps(data, indent=2, sort_keys=True)
    open(path, 'w').close()
    with open(path, "w") as f:
        f.write(products_json)

    print("Done")


def sort_by_sold(productList):
    return productList.sort(key=lambda x: x.count, reverse=True)


def best_sellers(k):
    return k['sold']


page = read_page(URL)
soup = BeautifulSoup(page, "html.parser")
page_count = get_page_count(soup)


page_count = int(page_count)


def clear_console():
    os.system('clear')


def write_data_to_file():
    products.sort(key=best_sellers, reverse=True)
    print(json.dumps(products, indent=4, sort_keys=True))
    write_to_file(dirname + "/results/" + shop_name + ".txt", products)


clear_console()
# for page_number in range(1, page_count):
#     try:
#         print("Reading page #: " + str(page_number) + "/" + str(page_count))
#         page = read_page(URL_paginated + str(page_number))
#         soup = BeautifulSoup(page, "html.parser")
#         time.sleep(random.randint(15, 60))
#         add_products_to_json(get_product_list(soup))
#     except Exception as e:
#         logging.error(traceback.format_exc())
#         write_data_to_file()
#     finally:
#         print("Done!")

# write_data_to_file()


# def scrape_shop(shop_name):
#     page_content = get_shop(shop_name)
#     sold_page_content = get_shop_sold_page(shop_name)


# scrape_shop("EmilyEstherDesigns")


from array import array
from genericpath import isfile
import json
import os
from textwrap import indent
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import sys
from os import listdir, path, walk
from constants import *
from os.path import join
import glob
from error_handlers import *
from bs2json import bs2json

from scripts.soup_to_json import add_items_to_json

session = HTMLSession()
soup = {}
previous_scrape_results = {}
URL = "https://www.etsy.com/shop/"


def count_sell_count(product_title):
    global products
    try:
        for i in products:
            if product_title == products[i]['name']:
                return products[i]['sold'] + 1
        return 1
    except Exception as e:
        return 1


def is_error_page(scrape_soup):
    if (scrape_soup.find(class_="error-page-panel")):
        return True
    else:
        return False


def get_folder_contents(folder_path):
    arr = os.listdir(folder_path)
    if len(arr) > 0:
        return arr
    else:
        return False


def was_shop_scraped(shop_name, shops):
    match = [shop for shop in shops if shop_name in shop]
    if len(match) > 0:
        return match
    else:
        False


def get_shop_sold_page(shop_name):
    sold_page = URL + shop_name + "/sold"
    page = session.get(sold_page)
    soup = BeautifulSoup(page.content, "html.parser")

    if is_error_page(soup):
        raise NotFoundException("No sold info page")
    else:
        return soup


def get_items_list(soup):
    results = soup.find(class_="responsive-listing-grid")
    return results.find_all("div", class_="js-merch-stash-check-listing")


def get_page_count(soup):
    page_nav = soup.find(class_="clearfix")
    page_list = page_nav.find_all(
        "li", class_="btn btn-list-item btn-secondary btn-group-item-md hide-xs hide-sm hide-md")
    for page in page_list:
        if page == page_list[-1]:
            return int(page.find_all("span")[-1].get_text().strip())


def get_shop(shop_name):
    global soup
    page = session.get(URL + shop_name)
    soup = BeautifulSoup(page.content, "html.parser")
    if is_error_page(soup):
        return None
    else:
        return soup


def log(message):
    print(message, file=sys.stderr)


def get_sold_page(soup, shop_name):
    scraped_shops = get_folder_contents('./results')
    if scraped_shops:
        previous_results = was_shop_scraped(shop_name, scraped_shops)
        if previous_results:
            log(str(previous_results))
            with open("./results/" + previous_results[0], 'r') as f:
                previous_scrape_results = json.loads(f.read())
            log(
                previous_scrape_results[0].get('name')
            )

        else:
            sold_info_page = get_shop_sold_page(shop_name)
            page_count = get_page_count(sold_info_page)
            print(sold_info_page, file=sys.stderr)
            print(page_count, file=sys.stderr)
            # if page_count > 1:
            #     for page in range(5):
            #         print("ye", file=sys.stderr)
            # # items_list = get_items_list(sold_info_page)
            # # items_json = add_items_to_json(items_list)
            # pretty_json = json.dumps("items_json",
            #                          sort_keys=True, indent=2)
            return "pretty_json"

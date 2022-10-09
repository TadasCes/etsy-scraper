
from array import array
from genericpath import isfile
import os
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

session = HTMLSession()
soup = {}
previous_scrape_results = {}
URL = "https://www.etsy.com/shop/"

items_list = []


def get_sold_count(product_title):
    global products
    try:
        for i in products:
            if product_title == products[i]['name']:
                return products[i]['sold'] + 1
        return 1
    except Exception as e:
        return 1


def format_item(item):
    item_title = item.find(
        "h3", class_="wt-text-caption").text.strip()
    item_link = item.find("a", class_="listing-link")["href"]
    item_img = item.find(
        'div', class_="v2-listing-card__img").find('img')['src']
    item_sold = get_sold_count(item_title)
    return {
        'name': item_title,
        'link': item_link,
        'image': item_img,
        'sold': item_sold
    }


def is_item_in_list(item_json):
    global items_list
    for item in items_list:
        if item['name'] == item_json['name']:
            return True
    return False


def add_items_to_json(item_list):
    global items_list
    items_list = []
    for sold_item in item_list:
        item_json = format_item(sold_item)
        if (len(items_list) > 0):
            if (is_item_in_list(item_json) == False):
                items_list.append(item_json)
            else:
                for item in items_list:
                    if item['name'] == item_json['name']:
                        item['sold'] = item['sold'] + 1
        else:
            items_list.append(item_json)
    return items_list

import os
from bs4 import BeautifulSoup
import time
import random
from requests_html import HTMLSession
from pathlib import Path
import sys
session = HTMLSession()

dirname = os.path.dirname(__file__)


def get_shop_name(url):
    url_to_list = url.split("/")
    page_name = url_to_list[url_to_list.index('shop') + 1]
    return page_name


def read_page(url):
    shop_name = get_shop_name(url)
    f = open('results.txt')
    try:
        f = open(
            dirname + "/scraped-pages/" + shop_name + ".txt")
        return f.read()
    except IOError as e:
        page = session.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        if (soup.find(class_="responsive-listing-grid") is None):
            time.sleep(random.randint(30, 180))
            read_page(url)
        else:
            write_page_to_file(
                soup, dirname + "/scraped-pages/", shop_name)
            f = open("./scraped-pages/" + shop_name + ".txt")
            return f.read()
    finally:
        f.close()


def write_page_to_file(page, path_to_file, page_name):
    path = path_to_file + page_name + ".txt"
    f = open(path, 'w+')
    with open(path, "w") as f:
        f.write(str(page))
    print("Done")

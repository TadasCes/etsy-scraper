import sys
from xml.etree.ElementTree import tostring
import error_handlers
import json
import logging
import os
from flask import Flask, abort, jsonify
from flask import request
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException
from scripts.get_shop import get_shop
from error_handlers import *
from scripts.get_shop import get_sold_page
from scripts.get_shop import log

# from server.server import scrape_shop


app = Flask(__name__)
app.register_blueprint(error_handlers.blueprint)
cors = CORS(app)
app.run(debug=True)


def scrape_shop(shop_name):
    shop_data = get_shop(shop_name)
    if shop_data:
        shop_info = get_shop_main_info(shop_data)
        shop_listings = get_shop_listings(shop_data)
        log(shop_listings)

        # sold_page_soup = get_sold_page(shop_data, shop_name)
        return shop_listings
    else:
        raise NotFoundException("Shop not found")


def get_shop_main_info(soup):
    shop_info = []
    shop_location = soup.find("div",
                              class_="shop-location").find("span", class_="shop-location").text.strip()
    shop_title = soup.find(
        "h1", class_="wt-text-heading-01").text.strip()
    sales_review = soup.find("div", class_="shop-sales-reviews")
    total_sales = sales_review.find(
        "span", class_="wt-text-caption wt-no-wrap").find("a").text.strip().split(" ")[0]
    shop_rating = sales_review.find(
        "a", class_="reviews-link-shop-info").find("span", class_="wt-screen-reader-only").text.strip().split(" ")[0]
    total_reviews = soup.find(
        "div", class_="reviews-total").find(class_="clearfix").find_all("div")[2].text.replace("(", "").replace(")", "").strip()
    total_listings = soup.find(
        "ul", class_="wt-tab wt-flex-direction-column-md wt-bb-xs-none vertical-tabs").find_all("button", class_="wt-tab__item")[0].find("span", class_="wt-mr-md-2").text.strip()

    shop_info.append({"location": shop_location})
    shop_info.append({"title": shop_title})
    shop_info.append({"sales": total_sales})
    shop_info.append({"rating": shop_rating})
    shop_info.append({"total_reivews": total_reviews})
    shop_info.append({"total_listings": total_listings})
    return shop_info


def get_shop_listings(soup):
    shop_listings = []
    featured_listings_soup = soup.find(
        "div", class_="featured-products-area").find(attrs={"data-featured-products-default-grid": True}).find_all('div', class_="v2-listing-card")
    listings_soup = soup.find(
        attrs={"data-listings-container": True}).find_all('div', class_="v2-listing-card")
    featured_listings = format_featured_listings_to_array(
        featured_listings_soup)
    listings = format_listings_to_array(listings_soup)
    shop_listings.append({"featured": featured_listings, "listings": listings})
    return shop_listings


def format_featured_listings_to_array(listings):
    formated_array = []
    for listing in listings:
        listing_json = {}
        listing_img = listing.find(
            "div", class_="v2-listing-card__img").find("img")["src"]
        listing_title = listing.find(
            "h3", class_="v2-listing-card__title").text.strip()
        listing_price = listing.find(
            "span", class_="currency-value").text.strip()
        listing_link = listing.find(
            "a", class_="listing-link")['href']
        listing_json = {
            "title": listing_title,
            "price": listing_price,
            "img": listing_img,
            "link": listing_link
        }
        formated_array.append(listing_json)
    return formated_array


def format_listings_to_array(listings):
    formated_array = []
    for listing in listings:
        listing_json = {}
        try:
            listing_img = listing.find("img")['data-src'].split(" ")[0]
        except:
            listing_img = listing.find("img")['srcset'].split(" ")[0]
        listing_title = listing.find(
            "h3", class_="v2-listing-card__title").text.strip()
        listing_price = listing.find(
            "span", class_="currency-value").text.strip()
        listing_link = listing.find(
            "a", class_="listing-link")['href']
        listing_json = {
            "title": listing_title,
            "price": listing_price,
            "img": listing_img,
            "link": listing_link
        }
        formated_array.append(listing_json)
    return formated_array


@ app.route("/<shop_name>", methods=['GET'])
def get_shop_info(shop_name):
    return scrape_shop(shop_name)


logging.getLogger('flask_cors').level = logging.DEBUG

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)

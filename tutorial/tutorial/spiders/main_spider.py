import scrapy
import json
import pandas as pd
import numpy as np
import logging
import requests
import urllib.request

from scrapy.utils.log import configure_logging

"""
Author: TRAN QUANG HUY - HASUKI1194

The script is commonly for scrapping the JSON data from the mobile phone (Android, iOS) via 

API request using the scrapy library and pandas, numpy library for gathering and organizing 

the JSON data in good format.



COMMAND TO RUN SCRIPT:

scrapy crawl samplespider -a city_name="HCMC"

"""

import time
main_start_time = round(time.time())

configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='logs/log-{main_start_time}.log'.format(main_start_time=main_start_time),
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)


class SampleSpider(scrapy.Spider):
    """
    Start list of URL should be the first page of all the different coordinates
    """
    name = "samplespider"
    
	"""
		Set up the location of output file after the scrapping done.
	"""
    custom_settings = {
        'FEED_URI':'file:///Users/Admin/Documents/Result-{runtime}.jl'.format(runtime=main_start_time),
        'FEED_FORMAT':'jsonlines'
    }

    # The authorization key to access via API
    working_authorization_key = ""


	# Creating a list of coordinates position.
    city_configurations = {
        
  
        "HCMC":{
            "name":"HCMC",
            "latitude_start":10.376525,
            "latitude_end":11.176041,
            "longitude_start":106.389196,
            "longitude_end":107.053956,
            "latitude_increment":0.02,
            "longitude_increment": 0.02,
            "center_coordinate": (10.775745,106.693584)
        },

    }


    def start_requests(self):


        def generate_coordinates_list(configuration_blob=None):
            """
            Pass in configuration blob

            Output: list of tuples in a (latitude, longitude) format
            """

            latitude_start = configuration_blob["latitude_start"]
            latitude_end = configuration_blob["latitude_end"]
            longitude_start = configuration_blob["longitude_start"]
            longitude_end = configuration_blob["longitude_end"]
            latitude_increment = configuration_blob["latitude_increment"]
            longitude_increment = configuration_blob["longitude_increment"]


            list_of_latitude = np.arange(latitude_start, latitude_end, step=latitude_increment)
            list_of_longitude = np.arange(longitude_start, longitude_end, step=longitude_increment)

            generated_coordinates = [ (x,y ) for x in list_of_latitude for y in list_of_longitude]

            print(len(generated_coordinates))

            return generated_coordinates

		
        list_of_coordinates = generate_coordinates_list(configuration_blob=self.city_configurations[self.city_name])


        
        for latitude, longitude in list_of_coordinates:

			# URL for request the API
            url_root = """"""

			
            headers = {
				"authorization":self.working_authorization_key,
				"x-location":"{latitude},{longitude}".format(latitude=str(latitude), longitude=str(longitude)),
				"x-location-accuracy":"65.0",
				"Accept-Encoding":"br;q=1.0, gzip;q=0.9, deflate;q=0.8",
				"Accept-Language":"en-VN"
            }
            print (latitude, longitude)
            request = scrapy.Request(url=url_root, headers=headers, callback=self.parse,dont_filter=True)
            request.meta["orignal_headers"] = headers

            print("ITERATED",latitude, longitude)

            yield request       
        




    def parse(self, response):
        """
        This will scrape from Near Me location. 
		
		You can separate the good format by call actual information you need.
        """
        r_json = json.loads(response.body)

        yield {
             "extracted_merchant_code" : r_json
        }
        

        

    



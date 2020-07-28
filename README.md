# Sample Scrapping
## This is sample of basic scrapping API using Python

The sample is following by using Scrapy library.

The methodology is using the Scrapy library to request an API call to collect the information (JSON) in mobile platform (iPhone, Android).
You can using the software tool to trace the API information (Eg: Charles Proxy, Fiddler, etc)

Following the step below for your installing and running the scrapping.
I prefer installing the scrapy in virtual environment than installing directly in Python.
If you are usually using the Anaconda methods, you can't skip the step 1. Just open the Anaconda Prompt.

1/ You can follow the site below for installing the virtual enviroment in python: 
  https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
  
  - Windows
      The Python installers for Windows include pip. You should be able to access pip using:

      >> py -m pip --version
      >> pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)
      
      You can make sure that pip is up-to-date by running:

      >> py -m pip install --upgrade pip
      
      Then, install the virtual environment:
      
      >> py -m pip install --user virtualenv
      
      Create and activate the new environment:
      
      >> py -m venv #your-environment-name
      
      point to the location .\env\Scripts\activate and run activate.bat
      

  - Linux and macOS
      It’s recommended to use the system pip to bootstrap a user installation of pip:

      >> python3 -m pip install --user --upgrade pip
      
      Afterwards, you should have the newest pip installed in your user site:

      >> python3 -m pip --version
      >> pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)
      
      Install the virtual environment:
      
      >> python3 -m pip install --user virtualenv
      
      Create and activate the new environment:
      
      >> python3 -m venv #your-environment-name
      
      point to the location source env/bin/activate
 
2/ Install the Scrapy library and create the directory. 
  - In the black-screen coding, install the scrapy:
  
    + If you are using the virtual environment Python:
      >> pip install scrapy
  
    + If you are using the Anaconda Prompt:
      >> conda install -c conda-forge scrapy
  
  - You can create the directory by:
  
  >> scrapy startproject #name_your_project
  
3/ Copy my scrapy code "main_spider.py" in sample-scrapping/tutorial/tutorial/spiders/ to your directory in ./tutorial/spiders/.
  If you don't know the structure of Scrapy library, look at the link to find out:
  https://docs.scrapy.org/en/latest/intro/tutorial.html
  
  
4/ In my python main_spider.py, you need to configure the output file will come, API information (URL, authorization key, etc) and location (lattitude, longitude).

5/ Command to run (for example):

  >> scrapy crawl samplespider -a city_name="HCMC"


## Reference: 
  - Scrapy Documentation: https://docs.scrapy.org/en/latest/

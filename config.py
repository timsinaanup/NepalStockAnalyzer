import requests as rq
from bs4 import BeautifulSoup as bs
import json
import numpy as np
import pandas as pd
import time

#for dynamic js pages (fundamental signals, )
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from movie_scrapper.page_information_extraction import extract_movie_info
from movie_scrapper.scrapper import get_url_data, get_beautiful_soup_data


def data_processing_and_dataframe_creation(url):
    soup = get_beautiful_soup_data(get_url_data("https://www.adorocinema.com" + url))
    return pd.DataFrame(data=extract_movie_info(soup), index=[0])


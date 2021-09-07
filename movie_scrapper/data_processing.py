import pandas as pd
from movie_scrapper.page_information_extraction import extract_movie_info, get_movie_sites
from movie_scrapper.scrapper import get_url_data, get_beautiful_soup_data


def data_processing_and_dataframe_creation(url):
    soup = get_beautiful_soup_data(get_url_data("https://www.adorocinema.com" + url))
    return pd.DataFrame(data=extract_movie_info(soup), index=[0])

def get_all_movies_sites(i):
    url = f"https://www.adorocinema.com/filmes-todos/?page={i}"
    return get_movie_sites(get_beautiful_soup_data(get_url_data(url)))

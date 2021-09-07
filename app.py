import pandas as pd
from movie_scrapper.page_information_extraction import get_all_movies_sites
from movie_scrapper.data_processing import data_processing_and_dataframe_creation


def scrap_movie_database(n_pages=100):
    movie_data = []
    for i in range(n_pages):
        print(f"Scrapping page - {i}")
        
        movies_site = get_all_movies_sites(i + 1)
        movie_data += list(map(data_processing_and_dataframe_creation, movies_site))
    return movie_data


if __name__ == "__main__":
    df = scrap_movie_database(1000)
    df = pd.concat(df).reset_index(drop=True)
    df.to_csv("data/database.csv")


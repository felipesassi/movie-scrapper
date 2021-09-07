from movie_scrapper.data_processing import *


class TestDataProcessing:
    def test_data_processing_and_dataframe_creation(self):
        url = "/filmes/filme-270144/"
        df = data_processing_and_dataframe_creation(url)

        assert set(df.columns) == set(["title", "date", "synopsis"])

    def test_get_all_movies_sites(self):
        i = 0
        assert len(get_all_movies_sites(i)) == 15
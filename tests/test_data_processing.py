from movie_scrapper.data_processing import data_processing_and_dataframe_creation


class TestDataProcessing:
    def test_data_processing_and_dataframe_creation(self):
        url = "/filmes/filme-270144/"
        df = data_processing_and_dataframe_creation(url)

        assert set(df.columns) == set(["title", "date", "synopsis"])

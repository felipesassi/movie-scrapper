from movie_scrapper.scrapper import get_url_data, get_beautiful_soup_data
from movie_scrapper.page_information_extraction import *


class TestPageInformationExtraction:
    def test_get_movie_title(self):
        url = "https://www.adorocinema.com/filmes/filme-270144/"
        soup = get_beautiful_soup_data(get_url_data(url))

        assert get_movie_title(soup) == "Shang-Chi e a Lenda dos Dez Anéis"

    def test_get_movie_date(self):
        url = "https://www.adorocinema.com/filmes/filme-270144/"
        soup = get_beautiful_soup_data(get_url_data(url))

        assert get_movie_date(soup) == "2 de setembro de 2021"

    def test_get_movie_synopsis(self):
        url = "https://www.adorocinema.com/filmes/filme-270144/"
        soup = get_beautiful_soup_data(get_url_data(url))

        assert get_movie_synopsis(soup)[:36] == "Em Shang-Chi e a Lenda dos Dez Anéis"

    def test_get_movie_sites(self):
        url = "https://www.adorocinema.com/filmes-todos/"
        soup = get_beautiful_soup_data(get_url_data(url))

        assert get_movie_sites(soup)[0].split("/")[0] == ""

    def test_extract_movie_info(self):
        url = "https://www.adorocinema.com/filmes/filme-270144/"
        soup = get_beautiful_soup_data(get_url_data(url))

        assert set(extract_movie_info(soup).keys()) == set(
            ["title", "date", "synopsis"]
        )

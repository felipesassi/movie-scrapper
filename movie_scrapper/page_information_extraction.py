from movie_scrapper.scrapper import get_url_data, get_beautiful_soup_data


def get_movie_title(soup):
    try:
        return soup.find(class_="titlebar-title").get_text()
    except:
        return "NAN"


def get_movie_date(soup):
    try:
        return soup.find(class_="date").get_text().strip()
    except:
        return "NAN"


def get_movie_synopsis(soup):
    try:
        return soup.find(class_="content-txt").get_text().strip()
    except:
        return "NAN"


def extract_movie_info(soup):
    return {
        "title": get_movie_title(soup),
        "date": get_movie_date(soup),
        "synopsis": get_movie_synopsis(soup),
    }


def get_movie_sites(soup):
    try:
        sites = soup.find_all(class_="meta-title-link")
        return [sites[i].attrs["href"] for i in range(15)]
    except:
        return []



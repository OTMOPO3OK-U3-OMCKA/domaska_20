from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def dao_movie():
    dao_movie = MovieDAO(None)

    m1 = Movie(id=1, title="кабаны-налетчики")
    m2 = Movie(id=2, title="кабаны в Майами")

    dao_movie.get_one = MagicMock(return_value=m1)
    dao_movie.get_all = MagicMock(return_value=[m1, m2])
    dao_movie.create = MagicMock(return_value=Movie(id=2))
    dao_movie.update = MagicMock()
    dao_movie.delete = MagicMock()
    return dao_movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, dao_movie):
        self.movie_service = MovieService(dao_movie)

    def test_movie_service_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None

    def test_movie_service_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_movie_create(self):
        m = {
            "title": "кабаны-картёжники"
        }
        movie = self.movie_service.create(m)
        assert movie is not None

    def test_movie_update(self):
        m = {
            "id": 2,
            "title": "суперкабаны против боевых космических инвалидов"
        }
        movie = self.movie_service.update(m)
        assert movie is not None

    def test_movie_delete(self):
        self.movie_service.delete(2)

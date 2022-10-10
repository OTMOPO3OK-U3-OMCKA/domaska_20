from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO

from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def dao_genre():
    dao_genre = GenreDAO(None)

    g1 = Genre(id=1, name="вестерн")
    g2 = Genre(id=2, name="боевик")

    dao_genre.get_one = MagicMock(return_value=g1)
    dao_genre.get_all = MagicMock(return_value=[g1, g2])
    dao_genre.create = MagicMock(return_value=Genre(id=3))
    dao_genre.update = MagicMock()
    dao_genre.delete = MagicMock()
    return dao_genre


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, dao_genre):
        self.genre_service = GenreService(dao_genre)

    def test_genre_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_genre_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_genre_create(self):
        g = {
            "name": "комедия"
        }
        genre = self.genre_service.create(g)
        assert genre.id is not None

    def test_genre_update(self):
        g = {
            "id": 2,
            "name": "экшен"
        }
        genre = self.genre_service.update(g)
        assert genre is not None

    def test_genre_delete(self):
        self.genre_service.delete(2)

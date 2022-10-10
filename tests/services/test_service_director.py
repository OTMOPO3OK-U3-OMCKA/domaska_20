from unittest.mock import MagicMock

import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def dao_director():
    dao_director = DirectorDAO(None)

    d1 = Director(id=1, name="Jora")
    d2 = Director(id=2, name="Gocha")

    dao_director.get_one = MagicMock(return_value=d1)
    dao_director.get_all = MagicMock(return_value=[d1, d2])
    dao_director.create = MagicMock(return_value=Director(id=3))
    dao_director.update = MagicMock()
    dao_director.delete = MagicMock()
    return dao_director


class TestServiceDirector:
    @pytest.fixture(autouse=True)
    def director_service(self, dao_director):
        self.director_service = DirectorService(dao_director)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        director = self.director_service.get_all()
        assert type(director) is list
        assert len(director) == 2

    def test_create(self):
        d = {
            "name": "vaha"
        }
        director = self.director_service.create(d)
        assert director.id is not None

    def test_update(self):
        d = {
            "id": 2,
            "name": "goga"
        }

        director = self.director_service.update(d)

    def test_delete(self):
        self.director_service.delete(7)


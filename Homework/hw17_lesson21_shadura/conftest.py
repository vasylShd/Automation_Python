import pytest
from .hw12_lesson16_shadura import ElectroCar

@pytest.fixture
def electrocar():
    electrocar = ElectroCar('Nissan', 'Leaf', 'Grey', 'Hatchback', 'Electric', 120, 40, 150)
    electrocar.charge_time(10, 5)
    yield electrocar


import pytest

from base.api.materials_api import create_material, delete_material_api
from models.materials import DefaultMaterial


@pytest.fixture(scope='function')
def function_material() -> DefaultMaterial:
    material = create_material()
    yield material

    delete_material_api(material.id)

# TODO заполнить
from models.materials import DefaultMaterial, MaterialDict, UpdateMaterial
from utils.assertions.base.expect import expect


def assert_material(
        expected_material: MaterialDict,
        actual_material: DefaultMaterial | UpdateMaterial
):
    pass

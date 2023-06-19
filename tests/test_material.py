from http import HTTPStatus

import allure
import pytest

from base.api.materials_api import (create_material_api, delete_material_api,
                                    get_material_api, get_materials_api, update_material_api)
from models.materials import (DefaultMaterial, DefaultMaterialsList, MaterialDict, UpdateMaterial)

from utils.assertions.api.materials import assert_material
from utils.assertions.base.solutions import assert_status_code
from utils.assertions.schema import validate_schema


@pytest.mark.materials
@allure.feature('Materials')
@allure.story('Materials API')
class TestMaterials:
    @allure.title('Get materials')
    def test_get_materials(self):
        response = get_materials_api()
        json_response: MaterialDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultMaterialsList.schema())

    @allure.title('Create material')
    def test_create_material(self):
        payload = DefaultMaterial()

        response = create_material_api(payload=payload)
        json_response: MaterialDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_material(
            expected_material=json_response,
            actual_material=payload
        )

        validate_schema(json_response, DefaultMaterial.schema())

        delete_material_api(json_response['Items'][0]['id'])

    @allure.title('Get material')
    def test_get_material(self, function_material: DefaultMaterial):
        response = get_material_api(function_material.id)
        json_response: MaterialDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_material(
            expected_material=json_response,
            actual_material=function_material
        )

        validate_schema(json_response, DefaultMaterial.schema())

    @allure.title('Update material')
    def test_update_material(self, function_material: DefaultMaterial):
        payload = UpdateMaterial()

        response = update_material_api(function_material.id, payload=payload)
        json_response: MaterialDict = response.json()

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_material(
            expected_material=json_response,
            actual_material=payload
        )

        validate_schema(json_response, DefaultMaterial.schema())

    @allure.title('Delete material')
    def test_delete_material(self, function_material: DefaultMaterial):
        delete_material_response = delete_material_api(function_material.id)
        json_delete_material_response: MaterialDict = delete_material_response.json()

        get_material_response = get_material_api(function_material.id)

        assert_status_code(delete_material_response.status_code, HTTPStatus.OK)
        assert_status_code(get_material_response.status_code, HTTPStatus.OK)

        assert_material(
            expected_material=json_delete_material_response,
            actual_material=function_material
        )

        validate_schema(json_delete_material_response, DefaultMaterial.schema())

        assert get_material_response.json()['CountList'] == 0

import numpy as np
import pytest
import sys
sys.path.append('C:\Users\lilia\Downloads\VineyardComparison-main\make_profile')
sys.path.append('C:\Users\lilia\Downloads\VineyardComparison-main\app')
from folium import Polygon

#тест1
def test_mean_elevation():
    def get_mean_elevation(polygons):
        # тест с квадратной геометрией
        bounding_geometry = [[[-61.19, 18.89], [-61.19, 18.94], [-61.14, 18.64], [-61.14, 18.89], [-61.19, 18.89]]]
        expected_mean_elevation = 18.89
        actual_mean_elevation = get_mean_elevation(bounding_geometry)
        assert expected_mean_elevation == actual_mean_elevation

if __name__ == '__main__':
    pytest.main()

#тест2
def profile_mean_soil_content(polygons):
    # Определяем полигон 
    polygon = [[[-61.19, 18.89], [-61.19, 18.94], [-61.14, 18.64], [-61.14, 18.89], [-61.19, 18.89]]]
    expected_result = {"Sand": 39.521, "Clay": 23.936, "Organic Matter": 11.467, "Other": 4.789}

    # Вызываем функцию и сравниваем результаты
    result = profile_mean_soil_content(polygon)
    return result

def test_profile_mean_soil_content():
    def profile_mean_soil_content(polygons):
        # Вызов функции, полученные результаты сравниваем
        result = profile_mean_soil_content(Polygon(polygons))
        expected_result = {"Sand": 39.521, "Clay": 23.936, "Organic Matter": 11.467, "Other": 4.789}
        assert result == expected_result


if __name__ == '__main__':
    pytest.main()



#тест3
def test_mean_temp():
    def get_mean_temp(bounding_geometry):
        # Определяем геометрию
        bounding_geometry = [[[-61.19, 18.89], [-61.19, 18.94], [-61.14, 18.64], [-61.14, 18.89], [-61.19, 18.89]]]
        # функция определния средней температуры
        mean_temp = get_mean_temp(bounding_geometry)
        # проверка значения
        np.testing.assert_allclose(mean_temp, 57.2, atol=1e-1)

if __name__ == '__main__':
    pytest.main()
    
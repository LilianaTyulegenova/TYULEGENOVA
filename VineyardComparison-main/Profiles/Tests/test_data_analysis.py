import pytest
import sys
sys.path.appen('')
from folium import Polygon 

def test_meanelevation():
    def get_mean_elevation(polygons):
        bounding_geometry = [[[-122.38, 37.78],[-122.38, 37.88], [-122.28, 37.78], [-122.38, 37.78]]]
        expected_mean_elevation = 37.78
        actual_mean_elevation = get_mean_elevation(bounding_geometry)
        assert actual_mean_elevation == expected_mean_elevation

if __name__ == '__main__':
    pytest.main()


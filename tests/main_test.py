from azure_python_wheel_dabs_example.main import get_taxis, get_spark


def test_main():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5

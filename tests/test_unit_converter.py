import pytest

from unit_converter import converter, create_app


def test_length_convert():
    assert converter.length_convert(20, "in", "mi") == pytest.approx(
        0.00031565656565656563
    )


def test_length_convert_float_value():
    assert converter.length_convert(20.1, "yard", "mi") == pytest.approx(
        0.011420454545454546
    )


def test_weight_convert():
    assert converter.weight_convert(100, "mg", "oz") == pytest.approx(
        0.003527396194958041
    )


def test_weight_convert_float_value():
    assert converter.weight_convert(20.1, "pound", "g") == pytest.approx(
        9117.206637000001
    )


def test_temperature_convert():
    assert converter.temperature_convert(5, "f", "k") == pytest.approx(258.15)


def test_temperature_convert_float_value():
    assert converter.temperature_convert(80.24, "f", "c") == pytest.approx(26.8)


def test_same_unit():
    assert converter.length_convert(10, "meter", "meter") == pytest.approx(10.0)


def test_invalid_number():
    with pytest.raises(ValueError):
        converter.convert("length", "two", "m", "km")


def test_unknown_unit():
    with pytest.raises(ValueError):
        converter.is_valid_unit_system("weight", "mm", "stone")


def test_unit_does_not_match_unit_type():
    with pytest.raises(ValueError):
        converter.is_valid_unit_system("length", "kg", "m")


def test_index():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_convert():
    app = create_app()
    client = app.test_client()

    response = client.post(
        "/convert",
        data={
            "type": "length",
            "value": "1000",
            "from": "meter",
            "to": "kilometer",
        },
    )

    assert response.status_code == 200
    assert b"1" in response.data

length_units = {
    "millimeter": 0.001,
    "mm": 0.001,
    "centimeter": 0.01,
    "cm": 0.01,
    "meter": 1,
    "m": 1,
    "kilometer": 1000,
    "km": 1000,
    "inch": 0.0254,
    "in": 0.0254,
    "foot": 0.3048,
    "ft": 0.3048,
    "yard": 0.9144,
    "yd": 0.9144,
    "mile": 1609.344,
    "mi": 1609.344,
}

weight_units = {
    "milligram": 0.000001,
    "mg": 0.000001,
    "gram": 0.001,
    "g": 0.001,
    "kilogram": 1,
    "kg": 1,
    "ounce": 0.028349523125,
    "oz": 0.028349523125,
    "pound": 0.45359237,
    "lb": 0.45359237,
}

to_celsius = {
    "c": lambda x: x,
    "celsius": lambda x: x,
    "f": lambda x: (x - 32) * 5 / 9,
    "fahrenheit": lambda x: (x - 32) * 5 / 9,
    "k": lambda x: x - 273.15,
    "kelvin": lambda x: x - 273.15,
}

from_celsius = {
    "c": lambda x: x,
    "celsius": lambda x: x,
    "f": lambda x: x * 9 / 5 + 32,
    "fahrenheit": lambda x: x * 9 / 5 + 32,
    "k": lambda x: x + 273.15,
    "kelvin": lambda x: x + 273.15,
}

unit_types = {
    "length": length_units,
    "weight": weight_units,
    "temperature": to_celsius,
}


def is_valid_unit_system(unit_type, from_unit, to_unit):
    if "" in (from_unit, to_unit):
        raise ValueError("Enter units of measurement.")

    elif 2 != [
        unit in unit_system
        for unit in (from_unit, to_unit)
        for unit_system in unit_types.values()
    ].count(True):
        raise ValueError("Unknown units of measurement.")

    elif not all(unit in unit_types[unit_type] for unit in (from_unit, to_unit)):
        raise ValueError(
            "The unit of measurement does not match the selected measurement type."
        )


def convert(unit_type, value, from_unit, to_unit):
    if not value:
        raise ValueError("Enter number")

    try:
        value = value.replace(",", ".")
        value = float(value)

    except ValueError:
        raise ValueError("Numbers only")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    is_valid_unit_system(unit_type, from_unit, to_unit)

    match unit_type:
        case "length":
            result = length_convert(value, from_unit, to_unit)

        case "weight":
            result = weight_convert(value, from_unit, to_unit)

        case "temperature":
            result = temperature_convert(value, from_unit, to_unit)

    formatted_value = str(value).rstrip("0").rstrip(".") + from_unit
    formatted_result = str(result).rstrip("0").rstrip(".") + to_unit

    return f"{formatted_value} = {formatted_result}"


def length_convert(value, from_unit, to_unit):
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]


def weight_convert(value, from_unit, to_unit):
    value_in_kilogram = value * weight_units[from_unit]
    return value_in_kilogram / weight_units[to_unit]


def temperature_convert(value, from_unit, to_unit):
    value_in_celsius = to_celsius[from_unit](value)
    return from_celsius[to_unit](value_in_celsius)

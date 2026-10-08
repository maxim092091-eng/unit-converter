# unit-converter
Unit Converter is a web application for converting between different units of measurement.

## Avaible types

- Length: millimeter (mm), centimeter (cm), meter (m), kilometer (km), inch (in), foot (ft), yard (yd), mile (mi). 
- Weight: milligram (mg), gram (g), kilogram (kg), ounce (oz), pound (lb).
- Temperature: Celsius (°C), Fahrenheit (°F), Kelvin (K).

## Requirements

- Python 3.10+
- A modern web browser

## Technologies

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Testing:** pytest

## Installation

### Clone the repository

```bash
git clone https://github.com/maxim092091-eng/unit-converter.git
``` 

### Navigate to the project directory

```bash
cd unit-converter
``` 

### Create a virtual environment

#### On Windows

```bash
py -m venv .venv
```

#### On Linux/macOS

```bash
python3 -m venv .venv
```

### Activate the virtual environment

#### On Windows

```bash
.venv\Scripts\activate
```

#### On Linux/macOS

```bash
source .venv/bin/activate
```

### Install the project

```bash
python -m pip install .
```

## Usage

### Run the application

Start the application:

```bash
flask --app "unit_converter:create_app" run
```

Open the application in your browser:

http://127.0.0.1:5000

### Convert units

1. Select a measurement type.
2. Enter a value.
3. Enter the source and target units.
4. Click the "Convert" button.

## Project Structure

```text
unit-converter/
├── src/
│   └── unit_converter/
│       ├── __init__.py
│       ├── routes.py
│       ├── converter.py
│       ├── templates/
│       │   └── index.html
│       └── static/
│           ├── css/
│           │   └── style.css
│           ├── fonts/
│           │   ├── Inter-VariableFont_opsz,wght.ttf
│           │   └── OFL(Inter).txt
│           └── js/
│               └── script.js
├── tests/
│   └── test_unit_converter.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Test

Run the tests with:

```bash
pytest
```

## Project

This project was built following the [Unit Converter](https://roadmap.sh/projects/unit-converter) project requirements from Roadmap.sh.

## License

This project is licensed under the MIT License.

## Author

Created by [Maxim](https://github.com/maxim092091-eng)

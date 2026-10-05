from flask import Blueprint, render_template, request

from .converter import convert

main = Blueprint("main", __name__)


@main.route("/")
def index() -> str:
    return render_template("index.html", result=None, error=None)


@main.route("/convert", methods=["POST"])
def convert_units() -> str:
    result = None
    error = None

    try:
        unit_type = request.form["type"]
        value = request.form["value"]
        from_unit = request.form["from"]
        to_unit = request.form["to"]

        result = convert(unit_type, value, from_unit, to_unit)

    except ValueError as e:
        error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error,
    )

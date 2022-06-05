# Put your app in here.
from flask import Flask, request
app = Flask(__name__)

from operations import add, sub, mult, div

@app.route("/add")
def add_page():
    numbers = request.args
    first_num = int(numbers["a"])
    second_num = int(numbers["b"])
    addition = add(first_num, second_num)
    return f"<body>{addition}</body>"

@app.route("/sub")
def sub_page():
    numbers = request.args
    first_num = int(numbers["a"])
    second_num = int(numbers["b"])
    subtraction = sub(first_num, second_num)
    return f"<body>{subtraction}</body>"

@app.route("/mult")
def mult_page():
    numbers = request.args
    first_num = int(numbers["a"])
    second_num = int(numbers["b"])
    multiplication = mult(first_num, second_num)
    return f"<body>{multiplication}</body>"

@app.route("/div")
def sdiv_page():
    numbers = request.args
    first_num = int(numbers["a"])
    second_num = int(numbers["b"])
    division = div(first_num, second_num)
    return f"<body>{division}</body>"



# FURTHER STUDY ANSWER BELOW #

@app.route("/math/<calc>")
def calculate(calc):
    # storing functions inside dictionary #
    calc_dict = {'add': add, 'sub': sub, 'mult': mult, 'div': div}
    #getting request arguments from URL #
    numbers = request.args
    first_num = int(numbers["a"])
    second_num = int(numbers["b"])
    # getting requested calculation from dictionary and running it #
    calculation = calc_dict[calc](first_num, second_num)
    return f"<body> {calculation} </body>"

#!usr/bin/python3
from flask import render_template
from app import app
from app.methods import readdata


def main():
    pass

@app.route('/')
def hello_world():
    data = readdata()
    return render_template('start.html',title = 'Testdata', data = data)

if __name__ == "__main__":
    main()


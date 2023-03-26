from flask import Flask, request, render_template
import re

app = Flask(__name__, static_folder='staticFiles')


@app.route('/regexmatch')
def home_page():
    return render_template("main.html")


@app.route('/regexmatch', methods=['POST'])
def match_regrex():

    text_string = request.form['text_string']
    regular_expression = request.form['regular_expression']

    matches = re.findall(regular_expression, text_string)
    return render_template('result.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)

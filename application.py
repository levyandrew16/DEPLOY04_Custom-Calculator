from flask import Flask, render_template, request

application = app = Flask(__name__)


@app.route('/')
def main():
    return render_template("cal.html")


@app.route("/calculate", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    num3 = request.form['num3']
    operation = request.form['operation']

    if operation == 'add':
        result = float(num1) + float(num2) + float(num3)
        return render_template('cal.html', result=result)

    elif operation == 'subtract':
        result = float(num1) - float(num2) - float(num3)
        return render_template('cal.html', result=result)

    elif operation == 'multiply':
        result = float(num1) * float(num2) * float(num3)
        return render_template('cal.html', result=result)

    elif operation == 'divide':
        result = float(num1) / float(num2) / float(num3)
        return render_template('cal.html', result=result)
    else:
        return render_template('cal.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template("cal.html")

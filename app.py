from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/level1_1_1')
def level1_1_1():
    return render_template('level1_1_1.html')

@app.route('/level1_1_2')
def level1_1_2():
    return render_template('level1_1_2.html')

@app.route('/level1_1_3')
def level1_1_3():
    return render_template('level1_1_3.html')

if __name__ == ('__main__'):
    app.run(debug=True)
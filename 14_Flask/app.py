from flask import Flask, render_template, request, redirect, url_for

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html>  <H1> Welcome to Flask course </H1> </html>"

@app.route("/index", methods=['GET'])
def index_page():
    return render_template('index.html')

@app.route("/form", methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello: {name}"
    return render_template("form.html")

# GET/POST Activity
@app.route("/submit", methods = ['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello: {name}"
    return render_template("form.html")

# Variable rule
@app.route('/success/<int:score>')
def success(score):
    return f"The marks you got is {score}"

# Building URL dynamically
@app.route('/score/<int:score>')
def success_score(score):
    res = ''
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
    return render_template('result.html', results = res)


# Building URL dynamically
@app.route('/success_result/<int:score>')
def success_result(score):
    res = ''
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'
    exp = {'Score': score, 'res': res}
    return render_template('result1.html',results=exp)

# If condition 
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html', results = score )

# Dynamic url

@app.route('/fail/<int:score>')
def fail_if(score):
    return render_template('result2.html', results = score)

@app.route('/submit_new', methods=['POST','GET'])
def submit_new():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        physics = float(request.form['Physics'])
        history = float(request.form['History'])
        total_score = (science + maths + physics + history) /4
        return redirect(url_for('successif',score=total_score))
    else:
        return render_template('getresult.html')
        

@app.route("/about")
def about_page():
    return render_template('about.html')

print(__name__)
 
if __name__ == '__main__':
    app.run(debug=True)
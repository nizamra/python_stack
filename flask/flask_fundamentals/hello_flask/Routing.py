from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success():
    return "dojo"
@app.route('/hi')                           
def hi():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/say/<name>')
def hello(name):
    return "hi, " + name+"!"

@app.route('/repeat/<num>/<txt>')
def numtxt(num, txt):
    return (txt+" ")*int(num)

if __name__=="__main__":
    app.run(debug=True)
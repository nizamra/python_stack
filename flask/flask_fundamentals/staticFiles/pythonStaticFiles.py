from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hi/<inputnum>')                           
def hi(inputnum):
    return render_template("index.html", numberOfPies=int(inputnum))


if __name__=="__main__":
    app.run(debug=True)
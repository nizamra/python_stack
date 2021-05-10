from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello players!'

@app.route('/play')                           
def playit():
    return render_template("playground.html")

@app.route('/play/<num>')
def numtxt(num):
    return render_template("playnum.html",numberOfPies=int(num))

@app.route('/play/<num>/<color>')
def somethingToDo(num,color):
    return render_template("pnmclr.html",numberOfPies=int(num),backColor=color)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world(x=8,y=8,color1="red",color2="black"):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)

@app.route('/<x>')                           
def hi(x,y=8,color1="red",color2="black"):
    return render_template("index.html",x=int(x),y=y,color1=color1,color2=color2)

@app.route('/<x>/<y>')                           
def hix(x,y,color1="red",color2="black"):
    return render_template("index.html",x=int(x),y=int(int(y)/2),color1=color1,color2=color2)
@app.route('/<x>/<y>/<color1>/<color2>')
def hixy(x,y,color1,color2):
    return render_template("index.html",x=int(x),y=int(int(y)/2),color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)
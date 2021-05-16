from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key = 'GazzaUnderAttack'

@app.route('/')
def fanatic():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=1

    return render_template("index.html",count=session['count'])

@app.route('/addtwo')
def three():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=2
    return render_template("index.html",count=session['count'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/addnum',methods=["POST"])
def addingmore():
    if 'count' not in session:
        session['count']=0
    else:
        session['count']+=int(request.form['num'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
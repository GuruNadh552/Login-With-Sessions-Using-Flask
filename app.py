from flask import Flask, render_template, Response,request,redirect,url_for,session

app=Flask(__name__)
app.secret_key = "guru"

@app.route('/')
def index():
    if "user" in session:
        return redirect(url_for('user'))
    else:
        return redirect(url_for('login'))

@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        session.permanent = True
        user = request.form["uname"]
        session["user"] = user
        return redirect(url_for('user'))
    else:
        if "user" in session:
            return redirect('user')
    return render_template('login.html')
@app.route('/user')
def user():
    if "user" in session:
        return render_template("welcome.html",user = session['user'])
    else:
        return redirect(url_for('index'))
@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for('index'))
    
app.run(debug=True)

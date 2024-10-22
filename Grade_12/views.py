from flask import render_template, redirect, url_for, session   
from Grade_12 import app
from Grade_12.forms import SignUpForm, LoginForm, ResultForm
from Grade_12.models import  User, Result
from Grade_12 import db 
from flask_login import login_user, login_required, current_user


@app.route("/home")
@app.route("/") #indexc route takes you to the landing page 
def index():    #creating a function for the route/url
    return render_template("index.html") #the function renders the template index.html

@app.route("/signup", methods=["GET", "POST"])   #sign up route/url with methods get and post 
def signup():
    form = SignUpForm() #creating an instance of the signup form from the signup class
    
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("index"))

    users = User.query.all()

    return render_template("signup.html", form=form, users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()

        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for("dashboard"))
            
            else:
                return redirect(url_for("login"))
            
        else:
            return redirect(url_for("login"))

    return render_template("login.html", form=form)

# DASHBOARD
@app.route("/dashboard", methods=["GET", "POST"] )
def dashboard():
    users = User.query.all()
    super_user = User.query.filter_by(username="onkiratu").first()
   
    return render_template("dashboard.html", users=users, super_user=super_user)
 

@app.route("/profile", methods=["GET", "POST"])
def profile():
    user = current_user
    return render_template("profile.html", user=user)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear   
    
    return redirect(url_for("index"))

# RESULTS 
@app.route("/result", methods=["GET", "POST"]) # 
def result():

    form = ResultForm()
    if form.validate_on_submit():
        student_id = form.id.data
        math = form.math.data
        english = form.english.data
        applied_computing = form.applied_computing.data
        algorithmics = form.algorithmics.data
        total_marks = math + english + applied_computing + algorithmics
        
        grade = ""
        average = total_marks/4

        if average  >= 70:
            grade = "A"
        
        elif average >= 60:
            grade = "B"

        elif average >= 50:
            grade = "C"

        elif average >= 40:
            grade = "D"
        
        else:
            grade = "F"
        

        result = Result(student_id=student_id, math=math, english=english, applied_computing=applied_computing, algorithmics=algorithmics, total_marks=total_marks, grade=grade)
        db.session.add(result)

       
        db.session.commit()
        return redirect(url_for("dashboard")) 
        
    return render_template("result.html", form=form)

def clear_table():
    db.session.query(Result).delete()
    db.session.commit()

@app.route("/clear_table")
def clear_table_route():
    clear_table()

    return redirect(url_for("dashboard"))
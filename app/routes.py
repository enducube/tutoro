from flask import render_template, request


from app import login_manager, login_user, logout_user, current_user, login_required, app, redirect, db
from app.models import SectionForm, Tutorial, Section, User, LoginForm, SaveForm


@login_manager.user_loader
def load_user(user):
    return User.query.get(user)

@app.route("/")
def index():
    return render_template("index.html", current_user=current_user)

@app.route("/register", methods=('GET', 'POST'))
def register():
    form = LoginForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user) # automatically log in the user
        return redirect("/")
    return render_template("register.html", form=form)

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template("login.html",form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/user/<str:username>")
def user(username):
    pass

@app.route("/createtutorial")
@login_required
def createtutorial():
    new_tutorial = Tutorial(title="unnamed tutorial",author=current_user.id)
    db.session.add(new_tutorial)
    db.session.commit()
    print(new_tutorial.id)
    return redirect("/edit/"+str(new_tutorial.id))

@app.route("/tutorial/<int:id>")
def viewtutorial(id):
    t = Tutorial.query.filter_by(id=id).first()
    sections = Section.query.filter_by(parentid=id)
    author = User.query.filter_by(id=t.author).first()
    return render_template("tutorial.html",tutorial=t,sections=sections,author=author)

@app.route("/edit/<int:id>", methods=("GET","POST"))
@login_required
def edit(id):
    addsection = SectionForm()
    saveform = SaveForm()
    if addsection.validate_on_submit():
        new_section = Section(type=addsection.type.data, parentid=id)
        db.session.add(new_section)
        db.session.commit()
    t = Tutorial.query.filter_by(id=id).first()
    sections = Section.query.filter_by(parentid=id)
    
    return render_template("edit.html",tutorial=t,asform=addsection,sections=sections, saveform=saveform)

@app.route("/save", methods=["GET","POST"])
def save():
    if request.method == "POST":
        #print(request.form.to_dict())
        savedsections = request.form.to_dict()
        sections = Section.query.filter_by(parentid=request.form['id']).all()
        print(savedsections)
        for i in sections:
            i.content = savedsections[str(i.id)]
        db.session.commit()
    return ''

            
        
from app import db, UserMixin, generate_password_hash, check_password_hash, StringField, PasswordField, InputRequired, FlaskForm, SelectField
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def set_password(self, password):
        self.password = generate_password_hash(password,method="sha256")
    def check_password(self, password):
        return check_password_hash(self.password, password)


class Tutorial(db.Model):
    __tablename__ = "tutorial"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.Integer)

class Section(db.Model):
    __tablename__ = "section"
    id = db.Column(db.Integer,primary_key=True)
    parentid = db.Column(db.Integer)
    type = db.Column(db.String)
    content = db.Column(db.String)
    

class LoginForm(FlaskForm):
    username = StringField(InputRequired())
    password = PasswordField(InputRequired())

class SectionForm(FlaskForm):
    type = SelectField(u'Type of section',choices=[('text','Text'),('image','Image')])

class SaveForm(FlaskForm):
    pass
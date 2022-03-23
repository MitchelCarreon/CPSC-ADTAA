from os import access
from app import db, ma
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    accessLevel = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)

    # properties for email confirmation
    email_confirmation_sent_on = db.Column(db.DateTime, nullable=True)
    email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    email_confirmed_on = db.Column(db.DateTime, nullable=True)

    # Valid user?
    isValid = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email_confirmation_sent_on = datetime.now()

    def __repr__(self):
        return f'User-> Email:{self.email}, Username:{self.username}, Access Level:{self.accessLevel}, Password:{self.password}'

# Generate marshmallow Schemas from your models


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "username", "email", "accessLevel")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# class Articles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100),nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime(), default=datetime.utcnow)


#     def __repr__(self):
#         return "<Articles %r>" % self.title

# # Generate marshmallow Schemas from your models
# class ArticlesShema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ("id","title", "body", "date")


# article_schema = ArticlesShema()
# articles_schema = ArticlesShema(many=True)

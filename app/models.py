from datetime import datetime
from hashlib import md5
from app import app,db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#association table for the many to many relationship that tracks folowers/followed
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(UserMixin, db.Model):
    #user properties
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    #print function
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #avatars done through gravatar
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    #add or remove followers
    def follow(self,user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self,user):
        if self.is_following(user):
            self.followed.remove(user)
    
    def is_following(self,user):
            return self.followed.filter(followers.c.followed_id==user.id).count()>0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id==Post.user_id)).filter(
                followers.c.follower_id==self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())  

    #declare many to many relatonship
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')    

#each user has an id
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#one to many relationship between users and posts, user_id is the foreign key
class Post(db.Model):
    #post properties
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(5000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    #print function
    def __repr__(self):
        return '<Post {}>'.format(self.body)
    

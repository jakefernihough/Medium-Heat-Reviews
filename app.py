import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Search bar
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("new_reviews.html", reviews=reviews)


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if username exists in db
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "email": request.form.get("email").lower,
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!, Please edit your profile!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile page
@app.route("/profile")
def profile():

    if session["user"]:
        user_profile = mongo.db.users.find_one(
            {"username": session["user"]})
        submitted_by = mongo.db.reviews.find(
            {"submitted_by": session["user"]})

        return render_template('profile.html',
                               user=user_profile, 
                               review=submitted_by)


# Edit Profile
@app.route("/edit_profile/<user_profile_id>", methods=["GET", "POST"])
def edit_profile(user_profile_id):

    if request.method == "POST":
        submit = {"$set": {
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
            }
        }
        mongo.db.users.update_one({"_id": ObjectId(user_profile_id)}, submit)
        session["user"] = request.form.get("username")
        flash("profile successfully updated!")

        return redirect(url_for("profile"))

    user_profile = mongo.db.users.find_one({"_id": ObjectId(user_profile_id)})
    return render_template(
        "edit_profile.html", main_content="edit_profile",
        user=user_profile)


# Logout
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# New Reviews Page
@app.route("/new_reviews")
def new_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("new_reviews.html", reviews=reviews)


# Add Reviews
@app.route("/add_reviews", methods=["GET", "POST"])
def add_reviews():
    if request.method == "POST":
        review = {
            "img_url": request.form.get("img_url"),
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "release_date": request.form.get("release_date"),
            "created_by": request.form.get("created_by"),
            "genre": request.form.get("genre"),
            "length": request.form.get("length"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "submitted_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Submitted")
        return redirect(url_for("new_reviews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_reviews.html", categories=categories)


# Edit Reviews
@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "img_url": request.form.get("img_url"),
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "release_date": request.form.get("release_date"),
            "created_by": request.form.get("created_by"),
            "genre": request.form.get("genre"),
            "length": request.form.get("length"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "submitted_by": session["user"]
        }
        mongo.db.reviews.update({'_id': ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_review.html", review=review,
                           categories=categories)


# Delete Reviews
@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("new_reviews"))


# Categories page
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Films Page
@app.route("/films")
def films():
    reviews = mongo.db.reviews.find()
    return render_template("films.html", reviews=reviews)


# TV Page
@app.route("/television")
def television():
    reviews = mongo.db.reviews.find()
    return render_template("television.html", reviews=reviews)


# Books Page
@app.route("/books")
def books():
    reviews = mongo.db.reviews.find()
    return render_template("books.html", reviews=reviews)


# Video Games Page
@app.route("/videogames")
def videogames():
    reviews = mongo.db.reviews.find()
    return render_template("videogames.html", reviews=reviews)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)

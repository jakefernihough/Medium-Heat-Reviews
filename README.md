![Medium Heat Reviews](/static/images/logo.jpg)

# Medium Heat Reviews


[Medium Heat Reviews](https://medium-heat-reviews.herokuapp.com/) is an interactive Media review app where its users
can create a register and login to a profile, which from there they can update it and fill out some information about themselves
including their favourite film, tv show, book and video game. They can read other users reviews and even create, edit and delete their own for
others to see.

As someone who has dedicated a lot of education towards media, I felt that I'd love to tell people more
about the things I discover and see how they fare in other peoples eyes.
So to be able to want to find a new book to read, I can look at what other people recommend so that I can experience
what they enjoy or what they're passionate about.

[live site](https://medium-heat-reviews.herokuapp.com/)

![website](/static/images/website.jpg)

## Contents ##

- [UX](#ux)
  - [**Project Goals**](#project-goals)
  - [**Site Owner Goals**](#site-owner-goals)
  - [**User Stories**](#user-stories)
      - [Site Visitor](#site-visitor)
      - [Registered User](#registered-user)
  - [**User Requirements and Expectations**](#user-requirements-and-expectations)
      - [Requirements](#requirements)
      - [Expectations](#expectations)
  - [**Design Choices**](#design-choices)
      - [Fonts](#fonts)
      - [Colours](#colours)
  - [**Wireframes**](#wireframes)
      - [Site Layout](#site-layout)
      - [Wireframes Links](#wireframes-links)
      - [Database Design](#database-design)
      - [Data Storage Types](#data-storage-types)
  - [**Technologies**](#technologies)
      - [Languages](#languages)
      - [Libraries and Tools](#libraries-and-tools)
  - [**Features**](#features)
      - [Current Features](#current-features)
      - [Future Features](#future-features)
  - [**Changes Applied since Development**](#changes-applied-since-development)
      - [Filtered Features](#fitered-features)
      - [Admin Features](#admin-features)
      - [Rating System](#ratingsystem)
      - [Categories Page](#categories-page)
  - [**Testing**](#testing)
  - [**Deployment**](#deployment)
      - [Cloning from GitHub](#cloning-from-github)
      - [Deploying to Heroku](#deploying-to-heroku)
  - [**Credits**](#credits)
      - [Images](#images)
      - [Cards](#cards)
      - [Code Ideas](#code-ideas)
  - [**Acknowledgements**](#acknowledgements)


# UX

## Project Goals

The goals for the website are :

* Create an interactive app/website where new users can **create an account**
* Once registered/ logged in, users can then **edit** their *profile*, **add** reviews,
**edit** reviews, **read** other users reviews, as well as **delete** their own reviews.
* To provide different content functionailities for users and potential users.
* For the app to store required data that is readily available for access and editing when and if required.

## Site Owner Goals

* To provide a site that promotes personal reviews about peoples favourite media and giving reasons as to why they enjoyed it so much.
* Build a community of Media enthusiasts.
* To build upon the site and create a more interactive community, where forums will help user chat to other users (future goal)

[Back to Contents](#contents)

---

## User Stories

### Site Visitor

* As a user, I want to be able to find out about what the app **provides**.
* As a user, I want to be able to be able to **Register** for a new account.
* As a user, I want to be able to find **social media** acounts connected to the app.

### Registered User

* As a user, I want to be able to **login** to my account.
* As a user, I want to be able to **edit** my profile.
* As a user, I want to be able to **logout** of my account.
* As a user, I want to be able to discover the **latest reviews**.
* As a user, I want to be able to find reviews for specific **categories**.
* As a user, I want to be able to **read** other users reviews.
* As a user, I want to be able to **add** my own reviews.
* As a user, I want to be able to **find** my reviews on my profile.
* As a user, I want to be able to **edit** my reviews.
* As a user, I want to be able to **delete** my reviews.

[Back to Contents](#contents)

---

## User Requirements and Expectations

### Requirements

* Visually pleasing design.
* Easy Navigation.
* Content information is displayed in a simple and clear way on all devices.
* Easy to use buttons where text is absent.

### Expectations

* User information is protected.
* Quick loading time.
* Ease of use when accessing the websites elements.

[Back to Contents](#contents)

---

## Design Choices

The aim of the website was to promote the media reviews. I wanted the site to stand out visually,
as it was common through my research for flashy colours. However I decided on using just 3 colours
that complimented each other well.

### Fonts 

I chose one font throughout the website to give it a consistent feel.

* Font Used
   > font-family: 'JetBrains Mono', monospace;

### Colours

I decided on using 
> rgb(36,0,26)

as the main focus colour with a yellow font due to the fact it made everything
stand out better for the users.

[Back to Contents](#contents)

---

# Wireframes

## Site Layout

I created a design plan about how I wanted the app to look.
Using [Balsamiq](https://balsamiq.com/) to help design the site,
I used it to define the basic structure and layout on all devices.

### Wireframes Links

You can view all the wireframes [here](/static/wireframes/app-design)
Or alternatively you can find the [PNG's Here](https://drive.google.com/drive/u/0/folders/155fhjc8IKK8h0c0IM9ql_E2Mx9DR4HLG)
As well as the [PDF File](https://drive.google.com/drive/u/0/folders/1gnHhoQt52utiunmTVCdYbGpKiU4Xfplz)

## Database Design

From learning the NoSQL features through MongoDB, I was able to map out the following
collections that were key to creating my website.

### Users Collection

**Title**|**Key**|**Data Type**
:----:|:----:|:----:
User ID|_id|ObjectId()
Username|username|string
Email|email|string
Password|password|string
Name|name|string
Favourite Film|favourite_film|string
Favourite TV Show|favourite_tv_show|string
Favourite Book|favourite_book|string
Favourite Game|favourite_game|string
Tagline|tagline|string

### Categories Collection

**Title**|**Key**|**Data Type**
:----:|:----:|:----:
Categories ID|_id|ObjectId()
Category NAme|category_name|string

### Reviews Collection

**Title**|**Key**|**Data Type**
:----:|:----:|:----:
Reviews ID|_id|ObjectId()
Image Url|img_url|string
Category Name|category_name|string
Title|title|string
Release Date|release_date|string
Created By|created_by|string
Genre|genre|string
Length|length|string
Review|review|string
Rating|rating|string
Submitted By|submitted_by|string

### Data Storage Types

MongoDB utilises the following data:

* ObjectId
* String
* Object
* Boolean
* Binary
* Array

[Back to Contents](#contents)

---

# Technologies

## Languages

* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)

## Libraries and Tools

* [Heroku](https://dashboard.heroku.com/apps)
* [JQuery](https://jquery.com/)
* [Bootstrap](https://getbootstrap.com/)
* [MongoDB Atlas](https://www.mongodb.com/1)
* [PyMongo](https://pymongo.readthedocs.io/en/stable/index.html)
* [Flask](https://www.fullstackpython.com/flask.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Font-Awesome](https://fontawesome.com/)
* [Git](https://git-scm.com/)
* [Google Fonts](https://fonts.google.com/)
* [GitHub](https://github.com/)
* [Gitpod](https://gitpod.io/workspaces/)
* [Colour Picker](https://www.w3schools.com/colors/colors_picker.asp)
* [Bootsnipp](https://bootsnipp.com/)
* [Materialize](https://materializecss.com/)

[Back to Contents](#contents)

---

# Features

## Current Features

* **Responsive Design** - It is mainly to be used via a mobile, though it was the last thing I managed
to get responsive. Mobile is usually everyones first mode of access.

* **Slider** - on the home page, it scrolls through what the site has to offer.

* **Register** - Ability to register an account, using a *username*, *password* and *favourite quote*.

* **Log In/ Out** - Ability to log in as a current user and log out of the users session.

* **Edit Profile** - Ability to edit profile to make it more personal to the user.

* **Search Function** - Able to search for a specific category or title.

* **Add/Edit Review** - Ability to add a review and alter it if needed.

## Future Features

* **Rating System** - Ability to rate other peoples reviews.

* **Filtered Results** - Ability to filter search results for more specificity.

* **Comments** - Ability for other reviewers to add their comments to a review.

* **View Others Profiles** - Ability to look at other peoples profiles and find out more about that user.

* **Site Admin Flagged** - Ability for users to flag a user/review to the admin for inappropriate reviews.

[Back to Contents](#contents)

---

## Changes Applied since development.

### Filtered Features

* I was planning on having the users have the ability to filter through the reviews
(title, genre, rating etc), however due to time being an issue for me, I decided to put it on the 
future features section to implement at a later date.

### Admin Features

* My original plan was to have a flagging system available for the admin to view, but will have to be on the future 
features due to time constraint.

### Rating System

* I was originally thinking about having flames instead of stars to rate titles,
to go with the website name, however decided on stars for the time being.

### Categories Page

* I originally had the *"choose your category"* as its own seperate page, however I decided that
it didnt work well for the navigation and added in unneccessary steps. So decided to implement it
onto the new reviews page.

[Back to Contents](#contents)

---

# Testing

Testing information can be found in a separate [Testing.md](Testing.md) file.

[Back to contents](#contents)

# Deployment

*Medium Heat Reviews* was developed and built through GitHub, GitPod and Workspaces.

### Cloning from GitHub ###

**Ensure** you have the following installed:

- [Python 3](https://www.python.org/)
- [PIP](https://pypi.org/project/pip/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/)

**Create an account at [MongoDB](https://www.mongodb.com/).**

*WARNING: You may need to follow a different guide based on the OS you are using. For more information, read up [here](https://python.readthedocs.io/en/latest/library/venv.html)*

1: **Clone** the *Medium Heat Reviews* repository by either downloading from [source](https://github.com/jakefernihough/Medium-Heat-Reviews), or if you have Git installed typing the following command into your terminal:

git clone https://github.com/jakefernihough/Medium-Heat-Reviews)


2: **Navigate** to this folder in your terminal window and **install** required modules to run the application using the following command:

python -m pip -r requirements.txt

4: In MongoDB, create a new database called *MediumHeatDB* with three collections: *users*, *reviews*, and *categories*.

5: Back on your workspace, create a file to hold your environment variables and call it *env.py*.

5: Your env.py file should contain the following:

> import os

> os.environ.setdefault("IP", "0.0.0.0")

> os.environ.setdefault("PORT", "5000")

> os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")

> os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")

> os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")

> os.environ.setdefault("DEBUG", "1")

- Please make sure you update your **SECRET_KEY**, **password**, **database_name**, and **DATABASE_NAME**.

- Before pushing the project to a public repository, your env.py file should be added to .gitignore.

6: You can now run your application locally by typing the following command in your terminal:

python run.py

### Deploying to Heroku ###

1: **Login** to Heroku and create a new app.

2: **Create** a requirements.txt file using the following command:

pip3 freeze --local > requirements.txt

3: **Create** a Procfile with the following command:

echo web: python run.py > Procfile

4: **Push** these newly created files to your repository master.

5: **Add heroku remote** to your git repository by getting the heroku git URL from the heroku account settings. Then type the following: 

git remote add heroku https://git.heroku.com/your-heroku-repo

6: Push *Medium Heat Reviews* to your heroku:

git push heroku master

7: In your heroku app, **set** the following variables:

**Key**|**Value**
:-----:|:-----:
HOSTNAME|0.0.0.0
PORT|5000
MONGO_URI|YOUR_MONGODB_URI
SECRET_KEY|YOUR_SECRET_KEY

  ** Please make sure you enter your own *SECRET_KEY*, and *MONGO_URL*.

8: Click the deploy button on the Heroku dashboard.
9: The site has been deployed the Heroku.

[Back to contents](#contents)

# Credits

## Images

* For the logo, I created it through [FreeLogoDesign](https://www.freelogodesign.org/)
* Images were found in [Google Images](https://google.co.uk)

## Cards

* The category cards were found and designed from [FreeFrontend](https://freefrontend.com/css-cards/).

## Code Ideas

* The majority of the code and form functioanilty was took from [Code Institute](https://codeinstitute.net)'s Data Centric Development Mini Project,
and then styled specifically for my projects needs. **THANK YOU**

* [W3Schools](https://www.w3schools.com/) helped me with creating the scrollable effect on the cards.

* I got inspiration from this fellow [student](https://github.com/neringabickmore/scribbles) with help for how I wanted to layout my site.

[Back to contents](#contents)


# Acknowledgements 

I would like To thank these wonderful people for sticking by me during this project:

* My mentor [Adegbenga Adeye](https://www.linkedin.com/in/adegbenga-adeye-psm-i-14003635/) for being my saviour and my rock during this project.
Could not have gotten this far without him.

* [Code Institutes](https://codeinstitute.net) Tutors, who were absolutely kind and patient with me as I struggled to figure out concepts,
but walked me through it and gettinbg there in the end.

* My fellow Code Institutes Slack Community who helped me understand foreign concepts and applying them to my work.

* To my Friends who have constantly been testing my website and giving me advice about how to fix my issues. They've been absolute stars.

* To my aunt, who took me into her home as I was about to start the project and for keeping me on task through the difficult time and making sure i used my 
time wisely for how little I had to do this project.

You're the heroes!

[Back to contents](#contents)
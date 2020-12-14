![Medium Heat Reviews](/static/images/logo.jpg)

# Medium Heat Reviews - Testing

[live site](https://medium-heat-reviews.herokuapp.com/)
[README.md File](README.md)

![website](/static/images/website.jpg)

## CONTENTS

   - [**Automated Testing**](#utomated-testing)
       - [Validated Services](#validated-services)
       - [Testing Stories](#testing-stories)
           - [*Site Visitor*](#site-visitor)
           - [*Registered User*](#registered-user)
   - [**Manual Testing**](#maunual-testing)
       - [Testing](#testing)
       - [Additional Requirements and Expectations Testing](#additional-requirements-and-expectations-testing)
   - [**Bugs Discovered**](#bugs-discovered)
       - [Fixed Bugs](#fixed-bugs)


## Automated Testing

### Validated Services

- CSS File passed through [W3C CSS Validation Services](https://jigsaw.w3.org/css-validator/validator)
- HTML Files tested using [W3 validator](https://validator.w3.org). The errors that popped up were due to the code using python. Though managed to fix errors relating to HTML itself.
- Script.js passed validation through [jshint.com](https://jshint.com/)
- app.py was tested through [PEP8 validator](http://pep8online.com/checkresult) with no errors or complications.

[back to contents](#contents)

## Testing Stories

### Site Visitor

* As a user, I want to be able to find out about what the app **provides**.
    - The User is able to view what the app provides by clicking the *About Page* and the scroller goes through whats in store for them.
* As a user, I want to be able to be able to **Register** for a new account.
    - The user is able to navigate from the *About Page*, *Login Page* and the *Navbar* to find the registration page.
      The form will only be submitted once all inputs are filled out. displaying a *Green* line. User will get a prompt when *username* is already being used.
* As a user, I want to be able to find **social media** acounts connected to the app.
    - All Users can find the social links at the footer of the page.

### Registered User

* As a user, I want to be able to **login** to my account.
    - The user can navigate from the *About Page*, *Register Page* and the *Navbar* to find the *Login* page.
      The user must fill out the input correctly with their *username* and *password* otherwise a prompt will tell them it is not correct.
* As a user, I want to be able to **edit** my profile.
    - The User can edit profile as they log in as it will show on the first page. They are given new inputs to fill out to update their page. Can *cancel* it at any time.
* As a user, I want to be able to **logout** of my account.
    - The user can logout at any time through the *navbar*. A prompt will show if they have logged out *successfully*.
* As a user, I want to be able to discover the **latest reviews**.
    - The User can view the *Four latest reviews* submitted by users by clicking on the nav bar link.
* As a user, I want to be able to find reviews for specific **categories**.
    - The User can discover the categories section *underneath the new reviews* and the nav bar.
* As a user, I want to be able to **read** other users reviews.
    - The User can *read* the latest reviews on the new reviews page or search a specific category through the *search bar* or *category Nav link*
* As a user, I want to be able to **add** my own reviews.
    - The User can *add* their own reviews through the navbar or on their *profile*
* As a user, I want to be able to **find** my reviews on my profile.
    - The User can *find* their reviews on the *profile* page
* As a user, I want to be able to **edit** my reviews.
    - The User can *edit* their reviews on their *Profile*. All inputs will need to be entered for it to have been submitted correctly. Can cancel by pressing cancel button.
* As a user, I want to be able to **delete** my reviews.
    - The User can *delete* their reviews on the my reviews section on their profile.

[back to contents](#contents)

## Manual Testing

- **Responsive Design** 

The app has a different layout options, focused on *mobile-first* design in mind as more users are expected to use mobile rather than larger devices, such as a tablet or a laptop/desktop.

[back to contents](#contents)

### Testing

- **Slider** - About Page

Function works without the user having to interact.

- **Register** Account form

The user is able to create a new user account. The app will test if the username already exists or if it doesn't it allow the user to complete.

- **Login/Logout** Functionality

The user is able to login and logout from their account. If the user enters incorrect details when logging in they are notified to check the details.

- **Edit Profile** Functionality

The user is able to edit their profile by clicking on the button found on my profile. User must fill out all inputs for the form to be submitted.

- **Add/Edit Review** Functionality

The user is able to add a review, by clicking on the links found on my profile or the navbar and by filling out the desired inputs. Will have a prompt is successful.
The user can then edit it from their profile if they had made a mistake. A prompt will confirm if successfully edited.

- **Delete Review** Functionality

The user can delete their review on the profile - my reviews section by clicking the delete button icon. a messgae will appear if successful.

- **Search** Functionality 

The user can use the search bar to find a specific title or category. As well as use the category navigation for easier use.

[back to contents](#contents)

### Additional Requirements and Expectations Testing

- **Visually Pleasing Design**
   
   My friends and family enjoyed the colour scheme as it popped out at them and made them enjoy being on the page.

- **Easy Navigation**

The users are offered a simple and easy to follow navigation throughout the site by using text or icons when needed.

- **Content information displayed**

The users are pleased with a simple and organised design. Users found it easy to follow through with no added steps to take away from the simplicity.

- **Easy to use Buttons**

The users understood the button meanings where text was absent. As I used very common icons found throughout a lot of websites.

- **Protected USer information**

User information obtained through the site is not shared with third parties. Also, the user password is hashed when stored in the database.

- **User is able to manipulate elements of the page**

The user can click buttons on the page, enter information on the form inputs or select elements supplied on the forms.

- **Quick Loading Time**

The app functions fast. Minimal time delay when using the site.

[back to contents](#contents)

## Bugs Discovered

1. When registering/ logging in, Google Chrome has an issue that doesn't allow the website to be secure.

2. Viewing the code on Github. Edit_reviews/Add_reviews/login/register show the form not laid out neatly/ correctly, however on the workspace it is neatly coded.

![code format](/static/bugs/ogcode.png)
![format mess up](/static/bugs/image.png)

3. I attempted to change the text colour of the Form Select on add/edit reviews to choose category. I enlisted the help of 
Tutor Support and after 2 hours of changing class names, clearing cache, opening on incognito mode, we could not find a way to change the text colour.
I left the CSS at the bottom of the style.css file to show that it does attempt to change the colour.

![category choice fail](/static/bugs/fail.png)



### Solved Bugs ###

1. Admin was unable to login because I had written value="{{ user.password }}" in the edit profile section.
However once I removed that value, it worked perfectly fine. **FIXED**

                <div class="row">
                    <div class="input-field col s12">
                        <i class="fas fa-lock prefix yellow-text"></i>
                        <input id="password" name="password" minlength="4" maxlength="12"
                            pattern="^[a-zA-Z0-9{4,10}$" value="{{ user.password }} type="text" class="validate white-text" required>
                        <label class="white-text" for="password">Update Password</label>
                    </div>
                </div>

2. I put in the wrong Functionality so that my reviews would only show on that users profile.
After working with the Tutor, i managed to figure out the input. **FIXED**

   > submitted_by = mongo.db.reviews.find(
            {"submitted_by": session["user"]}).sort("_id", -1)

3. I only wanted to show the latest 4 reviews on the new reviews page. **FIXED**
 
   I first input this code:

    >  reviews = mongo.db.reviews.find().sort({"_id", -1}).limit(4)
    
    I realised after that the {} in the .sort function was not needed and it corrected my code.

[back to contents](#contents)
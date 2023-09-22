# Soulmate dating app

## Code institute milestone project three

![Project_image](app/static/documentation/project-preview.png)

Welcome to Soul Mate - the premier dating app designed to help you find meaningful connections and lasting love. Whether you're looking for a serious relationship, a fun date, or simply a new friend, Soul Mate is here to make the process enjoyable and successful.

## [View Soulmate on Heroku](https://soulmate-0737784650f0.herokuapp.com/)

Features

1. Profile Creation
   Create a profile that reflects your personality and interests.

2. Profile Editing
   Add a photo, Change your bio name and age in the settings reflected in your profile.

3. Dashboard 
   Find other users signed up on the soul mate database 

4. Favourites
   Add profiles from the dashboard to your favourites and find their full profiles instantly

5. Settings
   Customise your profile add a picture and details about yourself to your account

6. Search functionality
   Search through your favourite by specific parameters be it name or bio 

### User Stories

### As a new customer:

-   be able to create a new account as simply as possible taking a username and password
-   after signing up capture additional information such as hobbies and bio, tags for personal preferences
-   to be able to upload pictures to my profile
-   want to be able to add users to my favourites for future browsing

### As the business owner:

-   I would like to present a modern and attractive looking dating app
-   I would like the app to be desgined cleanly with a professional look
-   I would like navigation to be easy
-   I would like the sign up process to be easy 
-   I would like for users to be able to move through the database of other users
-   I would like for users to be able to favourite other accounts 
-   I would like for users to be able to update their details easily

### Strategy

Cretate a functional and high end dating app with all the features people have come to expect while improving on the concept.

## Structure of the website

Soulmate comprises of a login screen and a Registration page that leads to a dashboards containing multiple features such as a settings page that allows the user to alter their personal details as well as a favourites page that contains the liked individuals from the database.

## Wireframes

I used balsamiq to create the initial wireframes.

### Login Wireframes

![Desktop-Login-Wireframes](app/static/documentation/login-desktop-wireframe.png)

![Mobile-Login-Wireframes](app/static/documentation/login-mobile-wireframe.png)

### Registration Wireframes

![Desktop-Registration-Wireframes](app/static/documentation/register-desktop-wireframe.png)

![Mobile-Registration-Wireframes](app/static/documentation/register-mobile-wireframe.png)

### Dashboard Wireframes

![Desktop-Dashboard-Wireframes](app/static/documentation/dashboard-desktop-wireframe.png)

![Mobile-Dashboard-Wireframes](app/static/documentation/dashboard-mobile-wireframe.png)

### Favourites Wireframes

![Desktop-Settings-Wireframes](app/static/documentation/favourites-desktop-wireframe.png)

![Mobile-Settings-Wireframes](app/static/documentation/favourites-mobile-wireframe.png)

### Error Wireframes

![Desktop-Settings-Wireframes](app/static/documentation/error-desktop-wireframe.png)

![Mobile-Settings-Wireframes](app/static/documentation/error-mobile-wireframe.png)

### Error Wireframes

I chose a non-relational database for my dating app for this reason, rooted in the fundamental differences between relational and non-relational databases.

dating apps deal with diverse and unstructured user-generated content, which often doesn't fit neatly into the structured tables of relational databases. Non-relational databases offer the flexibility to adapt to changing data formats and requirements without the constraints of fixed schemas, making them better suited to handle this variability.

the decision to use a non-relational database was driven by the need for flexibility, scalability, and enhanced performance in managing unstructured data—qualities that make it the ideal choice for delivering a seamless and responsive dating experience compared to the more structured and rigid nature of relational databases.

![database-schema](app/static/documentation/database-structure.png)

### Colors

Main colours used in the project: 
hex #111827 for the background
hex #6366f1 for buttons and some links

### Images

-   Logos imagery and concepts for soul mate were created by myself using video and photo editing software such as adobe photoshop and capcut.

## logo design concepts
![Images](app/static/documentation/logo-concepts.png)

## login concept
![Images](app/static/documentation/concept-logins.png)

# Features

The website has the below features:

## Login

* #### The login screen is comprised of an input for email and password with a link that take users to a page allowing them to sign up and create an account

![project images](app/static/documentation/login-desktop.png)
![project images](app/static/documentation/login-tablet-mobile.png)


## Registraion
* #### The registration page is where users will create an account

    * The page consists of a username field and password field
    * An addition field is available for the user to confirm their password

![project images](app/static/documentation/register-desktop.png)
![project images](app/static/documentation/register-tablet-mobile.png)



## Dashboard

* The dashboard is the page a user will land on after signing in and comprises of the data for other users being show
* The user is able to forward their search randomly through other members of the dating app
* A favourite button is included to add a user to a favourites page for future browsing

![project images](app/static/documentation/dashboard-desktop.png)
![project images](app/static/documentation/dashboard-tablet-mobile.png)

## Favourites page

* The users favourited accounts will be kept in this page
* The user can remove accounts from this page by clicking on the unfavourite button
* The favourite page contains a search bar to search through your current favourites

![project images](app/static/documentation/favourite-desktop.png)
![project images](app/static/documentation/favourite-tablet-mobile.png)


## Settings page

* The user has access to multiple options allowing them to change their display picture, name and or bio
* The user is also able to delete their account and remove themselves from the database here

![project images](app/static/documentation/settings-desktop.png)
![project images](app/static/documentation/settings-tablet-mobile.png)


## Error page

* If the user encounters an error for any reason they will be redirected to this error page that then grants them the option to return to the dashboard

![project images](app/static/documentation/error-desktop.png)
![project images](app/static/documentation/error-tablet-mobile.png)

##  Future implementations

* Filters to specificy unique aspects of other users they which to find
* A messaging service for users to communicate
* Text compression to help performance
# Technologies used

### HTML5
* As a structure language.

### CSS
* As a style language.

### Javascript
* As a style language.

### Tailwind CSS 
* Tailwind 3.2 as a CSS framework to keep responsive, mobile first aproach.

### GitHub
* As a software hosting platform to keep project in a remote location.

### Heroku
* As a platform for hosting the app

### Mongo DB
* To store my database

### Flask
* As a framework to build the app

### Git
* As a version-control system tracking.

### Gitpod
* As a development hosting platform.

### Balsamiq
* As a wireframing tool.

### Photoshop CS2
* As an image editor.

# Testing

## Functionality testing 

 I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.

### Responsive test

 ![desktop-resolution-test](app/static/documentation/responsive.gif)



## Compatibility testing
 Site was tested across multiple virtual mobile devices and browsers. I checked all supported devices in Chrome developer tools. 
 
 I tested on hardware devices such as: Dell Latitude with Windows OS's, Huawei P30 smartphone with Android OS on google chrome browser and samsung A7 lite with Android OS.

## User stories testing

### As the Site Owner: 

-   I would like to present a modern and attractive looking dating app
      >Site loads into a modern login page powered by tailwind css
-   I would like the app to be desgined cleanly with a professional look
      >Site adheres to mordern design conventions and is responsive
-   I would like navigation to be easy
      >navigation layout is straight forward and simple to understand with the side bar and mobile burger
-   I would like the sign up process to be easy 
      >Sign up is fast an easy allowing the user to move straight to the dashboard upon creation of account
-   I would like for users to be able to move through the database of other users
      >User is capable of browsing randomly selected account on the dashboard
-   I would like for users to be able to favourite other accounts 
      >User has access to a favourite button that will move an account into their personal favourites page
-   I would like for users to be able to update their details easily
      >User has access to a variety of details they are able to change in the settings menu including, display picture, bio and name

### As a new customer:

-   be able to create a new account as simply as possible taking a username and password
      >Navigation to the registration page is easy and straight forward from the login page
-   after signing up capture additional information such as hobbies and bio, tags for personal preferences
      >User is able to upload a picture and enter their name for other account holder to see when browing the app
-   to be able to upload pictures to my profile
      >The user is able to upload and save a profile picture from the settings page
-   want to be able to add users to my favourites for future browsing
      >A favourites button is available under all other accounts allowing the user to move it into a personal favourites
-   be able to sort through my list of favourites
      > A search bar has been added in order to filter through the list of favourites for specifics regarding the names and bio's

## Issues found during site development

I had issues with the speed of the page loading on the favourites page due to the size of the images being uploaded, I rectified this by employing python code to compress the images and converting them to base 64 to be passed into the image fields

![testing_issue_1](app/static/documentation/base.png)
#

Initially after uploading the dummy data to the database the profile images were not synced with the correct names, this was rectified by the restructuring of the profile pic numbering style

![testing_issue_2](app/static/documentation/account-mismatched.png)
![testing_issue_2](app/static/documentation/reorganised.png)


#

An issue arose when logging out of the app whereby going back would put the user back onto the dashboard despite being logged out, this was correcte by use of a unique function that redirects the user back to the login page if the have logged out based on the presence of their username in the session

![testing_issue_3](app/static/documentation/logout-fix.png)
#


## Manual testing

I performed various exercises on the site attempting to break the order of movement through the app and checking that all error handling occured correctly

![manual_testing_1](app/static/documentation/errorcheckone.png)
![manual_testing_2](app/static/documentation/errorchecktwo.png)
![manual_testing_3](app/static/documentation/errorcheckthree.png)
![manual_testing_4](app/static/documentation/errorcheckfour.png)
![manual_testing_5](app/static/documentation/errorcheckfive.png)
![manual_testing_6](app/static/documentation/errorchecksix.png)

## Automated testing

By cloning locally and installing with
pip3 install -r requirements.txt

the user can run an automated test using selenium and field data generated by faker

![automated-test](app/static/documentation/selenium.gif)

## Performance testing
I run [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool to check performance of the website.

![performance test 1](app/static/documentation/performance-login-desktop.png)
![performance test 2](app/static/documentation/performance-login-mobile.png)
![performance test 3](app/static/documentation/performance-register-desktop.png)
![performance test 4](app/static/documentation/performance-register-mobile.png)
![performance test 5](app/static/documentation/performance-dashboard-desktop.png)
![performance test 6](app/static/documentation/performance-dashboard-mobile.png)
![performance test 7](app/static/documentation/performance-favourites-desktop.png)
![performance test 8](app/static/documentation/performance-favourites-mobile.png)
![performance test 7](app/static/documentation/performance-settings-desktop.png)
![performance test 8](app/static/documentation/performance-settings-mobile.png)




## Code Validation
 At the and of the project I used two websites to validate a code
 
 * [W3C CSS Validator]() to validate CSS
  ![Css-validation](app/static/documentation/css-validation.png)
  #


 * [Nu Html Checker](https://validator.w3.org/) to test HTML

  ![Html-validation-login](app/static/documentation/login-html.png)
  ![Html-validation-register](app/static/documentation/register-html.png)
  ![Html-validation-dashboard](app/static/documentation/dashboard-html.png)
  ![Html-validation-favourites](app/static/documentation/favourites-html.png)
  ![Html-validation-settings](app/static/documentation/settings-html.png)
  ![Html-validation-error](app/static/documentation/error-html.png)
  #
*  [jshint](https://jshint.com/) To error check javascript code
![Javascript-validation-part1](app/static/documentation/jshint1.png)
![Javascript-validation-part2](app/static/documentation/jshint2.png)

# Deployment

I used Gitpod as a development environment where I committed all changes to git version control system.

The application was deployed to heroku for the live site.

## Github Repository

https://github.com/Trollope91/Milestone-Project-three

## Live link

https://soulmate-0737784650f0.herokuapp.com/

## Copying the repository

A user can make a local copy of my repository by going to the GitHub repository page of my project and clicking on the "Code" button which will open a dropdown menu, select the protocol (HTTPS or SSH) for the clone URL and copy it to the clipboard.
Open a terminal on their local machine and navigate to the directory where they want to store the project then type the command "git clone" followed by the URL they copied in step 3, and press Enter.
Wait for the cloning process to complete.

## Clone link


## Forking the repository

To fork the repository the user can go to the GitHub repository page of the project and click on the "Fork" button in the upper right-hand corner of the page, select the account they want to fork the project to and then wait for GitHub to create a copy of the project in their account.
Once the fork is complete the project will be available under their account with the option to clone to their local machine.

___
# Credits


* To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

* Ideas and knowledge library:

    * [w3schools.com](https://www.w3schools.com)

    * [css-tricks.com](https://css-tricks.com/)

    * [python](https://www.python.org/)

    * [flask](https://flask.palletsprojects.com/en/2.3.x/)

    * [Stack Overflow](https://stackoverflow.com/)

    * [Tailwind CSS](https://tailwindcss.com/)

    * [mongodb](https://www.mongodb.com/)

    * [Selenium](https://www.selenium.dev/)

    * [Heroicons](https://heroicons.com/)

    * [CI Python Linter](https://pep8ci.herokuapp.com/#)

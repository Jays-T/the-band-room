# Welcome to <a href="http://the-band-room.herokuapp.com/the_band_room">The Band Room</a>

* This project is currently purely for educational purposes.
* I went with this idea because the future product that I envisage is an app that I personally want to be able to use for my Band.

# CONTENTS

* UX
  * <a href="#Owner-Goals">Owner Goals</a>
  * <a href="#User-Goals">User Goals</a>
  * <a href="#User-Stories">User Stories</a>
  * <a href="#My-Strategy">Strategy</a>
  * <a href="#Structure">Structure</a>
* <a href="#User-Interface">UI</a>
* <a href="#Features">Features</a>
* <a href="#Scope">Scope</a>
* <a href="#Information-Architecture">Information Architecture</a>
* <a href="#Defensive-Design">Defensive Design</a>
* <a href="#Technologies">Technologies Used</a>
* <a href="#Sources">Sites Sourced from</a>
* <a href="#Testing">Testing</a>
* <a href="#Bugs">Bugs</a>
* <a href="#Deployment">Deployment</a>
* <a href="#Credits">Credits</a>

<img src="/wireframes/responsive-900x544.png"/>

# **UX**

# Owner Goals

#### As the owner, my initial goals are:

* To quickly deliver to the user the basics of what the site has to offer
* To deliver basic CRUD functionality
* To create a platform that can easily be developed further with added features

#### Long-term goals for the owner are:

* To offer a full serviced one-stop solution to musicians looking to handle organizing their rehearsal/jam/event planning from one app and/or site

# User Goals

#### For the user the goals are:

* To be able to:
  1. quickly access and make use of the sites main services
  2. schedule an event, or multiple events, and check member availability
  3. make suggestions to band members via notes
  4. be notified whenever anything is updated (note posted, event suggested, song added, etc)
  6. track band progress in terms of song learning and writing, both individually and as a whole


# User Stories

1. "As a **band leader** I'm looking for a complete solution to scheduling and organizing my band activities."
2. "As a **band member** I'd like to have a clear idea of what to work on this week in preparation for our next rehearsal."
3. "As a **solo artist** having a progress tracker and a songlist that I can easily update and edit would be amazing."


# My Strategy

* My goal was to ensure the information was easy to access while striving for a responsive, simple and colorful design.
* I knew from the start that I would not have enough time to implement the various features that I have planned for the longterm.
* My idea for this site came out of frustration with my own Band while looking for a way in which we could organize ourselves and our planning better.
* I decided to focus on the fundamental basics for the app, CRUD functionality and Defensive Design. 

# Structure

<img src="/wireframes/bandroom-site-structure-380x463.png"/>

# User Interface

* Initial concept

<img src="/wireframes/the-band-room.png"/>

* I wanted the landing page to be simple and make it easy for the user to quickly get straight to the main purpose and service of the site.
* I wanted the site to convey the idea of a bit of fun rather than all work.
* Certain areas of the site are only accessible while logged in, this was done intentionally.
* The available links on the NavBar adapt according to whether the User is logged in or not. This is both to keep the interface as easy to navigate as possible and also a part of <a href="#Defensive Design">Defensive Design</a>.
* Certain features, such as the Add Song feature, the Add An Event feature, and the Contact page which are in the initial concept were not yet added and are now listed under <a href="#Features-still-to-implement">Features still to implement</a>

* I chose a single font which I felt matched well with the intended 'fun' feel of the site:
  * <a href="https://fonts.google.com/specimen/Bangers/" target="_blank">Bangers</a> 

# Features

- [x] Register User Account
- [x] Create Band Room
- [x] Browse Rooms
- [x] Edit Band Room
- [x] Delete Band Room

# Features still to implement

- [ ] Contact Page (allow the user to contact the site owner)
- [ ] Personalized Image for Band Room
- [ ] Delete User Account
- [ ] Calendar (I plan to possibly integrate <a href="https://fullcalendar.io/#demos" target="_blank">Full Calendar</a> )
- [ ] User availability confirmation (for events scheduled using the calendar)
- [ ] Add Band
- [ ] Invite and add Band members
- [ ] Invite Friends
- [ ] One to Many and Many to One accessibility such as:
  - [ ] One User is a member of multiple bands
  - [ ] One User able to access multiple Band Rooms (using relevant Room Key)
  - [ ] Mulitple Users able to access and Edit one Band Room (using relevant Room Key and Band Membership)
- [ ] Notifications via App
- [ ] Notifications via email
- [ ] Chat - Allow band members to chat to each other via the app
- [ ] Add Song to learn list
- [ ] Progress tracker (Song learning, Song writing, Set readiness, Gig readiness, Facebook Page likes, Instagram followers count)
- [ ] Song List - Songs ready for performing/recording
- [ ] Share Lyrics, share music, 
- [ ] Suggest Song
- [ ] Vote on suggested Song
- [ ] Add notes


# Scope

* The current scope of the project is limited, most of the intended features have yet to be implemented. The main reason for this is the limited time frame in which the initial educational project must be completed.
* Other reasons for the limited scope was because I wanted to take the time to focus on and implement the CRUD features of the site.
* Things like the Stock Image that I used for each band room will be replaced by the option for the User to provide a link to an Image of their choice.


# Information Architecture
* MongoDB Atlas is used for storing data for this web site.

* The following is the data structure. It is currently very basic.

**To store the Band Rooms**

```
{
    _id : ObjectId()
    owner_name : String,
    room_key : String,
    band_notes : String,
    social_media : String
}
```
**To store the Users**
```
{
    _id : ObjectId()
    username : String,
    user_key : Binary
}
```

# Defensive Design

* All the forms in this site have a validation system except for the Edit Room form. 
* Any submission with blank input is prevented and a message shown to inform users which neccessary input sections are empty.
* The Login function is only accessible via the UI if there is no current session, no one logged in.
* In case someone bypasses this by manually inputting the correct url route to the login page then:

* If there is already a user logged in, the route to the login_page will redirect to the user_landing and flash an error message:

* The Login function is designed to only allow a login if:
  1. There is no current session, no one logged in.
  2. The username exists.
  3. Both the username and password are correct and match each other in the database.
  4. If any of the criteria are not met, each of these safeguards will flash an error message to the user and redirect the route accordingly.
  5. If all these criteria are satisfied the app will allow the login.

* The Register function is only accessible via the UI if there is no current session, no one logged in.
* In case someone bypasses this by manually inputting the correct url route to the login page then:
* The Register function is designed to only allow a User to register if:
  1. There is no current session, no one logged in.
  2. If the request method is 'POST'(via the register form)
  3. If the chosen username does not already exist
  4. If any of the criteria are not met, each of these safeguards will flash an error message to the user and redirect the route accordingly.
  5. If all these criteria are satisfied the app will allow the user to register.

* The User area is only accessible if there is a current session, if a User is logged in.
* If there is no session, no user logged in, the app will flash an error message to the user and redirect them to the register page. I chose to redirect to the register page in case the user had no account as the links to login are also clearly visible on that page

* The Add Band Room page is only accessible via the UI if a User is in session.
* The function will only allow a User to create a room if the room_key is unique.
* The Add Band Room function however is not currently fully defensively designed. This is simply due to a lack of time and it is on the high priority list of next steps to take in development of this app.

* The Edit Room function is also not currently designed with safeguards and any user who is logged in can currently edit a Room.
* This means that any User can currently edit everything from the rooms Owner_name, the room_key etc.
* This means that a User could use the Edit function to edit the room_key, and then use that new room_key to delete the room.
* This will be fixed in the next iteration of this site. I have simply run out of time and am leaving it as is to demonstrate the CRUD functionality.
* Each of the validation steps included in the Login and Register functions will be included in future in the Add Band Room and Edit Band Room functions, including checking the room_key and matching the username with the room owner_name for further validation.

* The Delete Room function is only accessible via the UI if there is a current session, a user logged in.
* On the band room page there is a button named 'Delete'. On clicking this button the browser will flash an alert asking if the User is sure they want to delete the room.
* If the answer is no, the User can click on Cancel. If they are sure, they click Ok and this will then lead to a delete room form being shown. 
* The user must then input the correct room key and click a red 'Delete' button in order to call the delete room function.
* Once those steps have been fulfilled, then:
* The function is designed to only allow a User to delete if:
  1. There is a current session, a User is logged in.
  2. The Input Room Key is correct.
  3. If all these steps and criteria are satisfied the app will allow the user to delete the room.
* Matching of Username and Owner_name will be added in future to the defensive steps included in the Delete Room function.

* Currently on the band room page, even if the User clicks 'Cancel' on the alert asking if they are sure they want to delete the room, the delete room form will still be shown.
* This will be fixed in upcoming versions of this site. This doesn't actually lead to the room being deleted as the User still needs to input the correct Room_key and click the red delete button.
* But I would still like to have it designed so that if the User clicks Cancel, the delete form is not shown at all.

**Regarding DRY in the defensive design of the various functions**

* Only towards the end of this project did I come across a tutorial regarding using decorators within functions to protect endpoints.
* As I develop this project I will be writing better code as I learn more.
* For now I've tried to do my best with the knowledge I have currently. 

**Error Handling**

* I did not setup any error handling templates, such as a 404 template etc.
* Errors are handled using Flash messages and redirection to alternative app routes and endpoints.

# Technologies

* <a href="https://html.com/" target="_blank">HTML</a> - for overall UI structure
* <a href="https://css-tricks.com/" target="_blank">Css</a> - to style the site
* <a href="https://www.materializecss.com" target="_blank">Materialize</a> - for grid structure and responsive design, icons
* <a href="https://www.fontawesome.com" target="_blank">Font Awesome</a> - for social media icons
* <a href="https://www.python.com" target="_blank">Python</a> - for app routes and CRUD functionality
* <a href="https://jinja.palletsprojects.com/en/2.11.x" target="_blank">Jinja</a> - for templating, data routing and page information populating
* <a href="https://mongodb.com" target="_blank">MongoDB</a> - for the Database
* <a href="https://www.jquery.com/" target="_blank">jQuery</a> - used by Materialize and for the Register Form password compare function
* <a href="https://www.gitpod.io/" target="_blank">Gitpod</a> - as my development environment
* <a href="https://www.github.com/" target="_blank">GitHub</a> - for version control
* <a href="https://www.heroku.com" target="_blank">Heroku</a> - for deployment


# Sources

* <a href="https://www.w3schools.com">w3schools</a> - For general knowledge or whenever I was stuck on something simple
* <a href="https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ">Pretty Printed</a> - for help with developing the Register User function
* <a href="https://docs.mongodb.com/">MongoDB Docs</a> - for questions relating to database interaction
* <a href="https://blog.tecladocode.com/">Teclado Code Blog</a> - lots of great tips and tricks for Python and Flask
* <a href="https://css-tricks.com/">Css Tricks</a> - to solve styling and element placement issues
* <a href="https://fonts.google.com/">Google Fonts</a> - for fonts

# Testing

* Testing was done regularly throughout the entire process 
* Each function was tested and re-tested
* Defensive Design was tested by manually adding endpoints from areas where access should not be allowed
* All functions were tested using bogus usernames / passwords / room keys
* All functions were tested using correct usernames / passwords / room keys

* All HTML validated with <a href="https://validator.w3.org/">w3 validator</a>
* All CSS validated with <a href="https://jigsaw.w3.org/css-validator/">w3 css validator</a>

* I used various code and syntax checkers during the entire process and before project submission

**Checkers Used**
* <a href="https://extendsclass.com/python-tester.html">Python Syntax Checker</a>
* <a href="http://pep8online.com/">Python Checker</a>
* <a href="https://esprima.org/demo/validate.html">Esprima JavaScript Checker</a>
* <a href="https://jshint.com/">JsHint JavaScript Checker</a>

## This site has been tested manually

Browsers tested: 
* Chrome
* Microsoft Edge

Phones tested: 
* Huawei P20Lite
* iPhone 6
* Xaomi Mi 9

* Site also tested with Chrome's built in 'Inspect Element' preview panes simulating the iPad Pro, iPad, iPhone X, iPhone 6/7/8 plus, iPhone 6/7/8, iPhone 5 SE, Pixel 2 XL, Pixel 2 and Galaxy S5
* JS and jQuery code tested on <a href="https://www.repl.it" target="_blank">ReplIt</a>
* Entire site tested extensively with console log and print() - once functions/routes were found to be working as intended console.log and print() commands were removed
* All inter-site links tested on all pages across devices and found to be working
* All outward links directed at other sites tested and found to be working and opening in a new tab
* While watching the console log in real time, no major errors were found across the site

# Bugs

**Major Bugs**
* While developing the site I removed the link to the 0.100.2 version of the Materialize .js file. I replaced it with the latest version and stored the file locally in order to get the sidenav to show on clicking the menu button on small devices.
* This caused the tabs on the cards with multiple tabs to stop working. I found that the sidenav function needed the updated .js file from Materialize while the Card with Tabs only worked with the 0.100.2 version.
* I included both versions to solve the issue
**Minor Bugs**
* Minor Bug #1: With the login modal it seems the form input doesn't always respond well to touch screens on phone. 
* To solve this issue I removed all modals completely as I felt the experience was too frustrating.

* Minor Bug #2: In the console the site returns: Manifest: Line: 1, column: 1, Syntax error.
* I have not been able to solve this issue, but it does not affect the running of the site.

# Deployment

* This project and all project files are hosted on GitHub via my GitHub repository at <a href="https://github.com/Jays-T/the-band-room" target="_blank"></a>
* I coded the project using GitPod as my development environment. 
* This project is also hosted and deployed with Heroku
* To deploy the project using Heroku
   1. Register an account at <a href="https://heroku.com" target="_blank">Heroku</a>
   2. Go to Heroku site, login and create a new app. Set a name for this app and select the closest region.
   3. In the Deploy tab of your App dashboard in Heroku, choose Deployment method. I chose Heroku Git, using Heroku CLI and logged in via the terminal using the command: heroku login
   4. In GitPod, create a requirements.txt file using the command pip3 freeze > requirements.txt in the terminal.
   5. Create a Procfile using the commant echo web: python app.py > Procfile in the terminal.
   6. Login to Heroku via the terminal using command heroku login
   7. Commit your changes using: git add and git commit -m "commit message here"
   7. Push your changes using: git push heroku master
   8. In your Heroku Dashboard, Go to the Settings of your app and then Reveal Config Vars and set the values as follows (remove the spaces and '<'>'from the MONGO_URI):

   | KEY         | VALUE                                                                                         |
   | :---        | :---                                                                                          |
   | IP          | 0.0.0.0                                                                                       | 
   | PORT        | 5000                                                                                          |
   | MONGO_URI   | mongodb+srv://root:< your password >@cluster0-r5ils.mongodb.net/< your dbname >               |
   |             | ?retryWrites=true&w=majority                                                                  |
   | SECRET_KEY  | <your_secret_key>                                                                             |
   


## There are no differences between the currently deployed site and the development version at this time.

## To run the project locally

To clone this project from GitHub:

* Under the repository name, click "Clone or download".
  1. In the Clone with HTTPs section, copy the clone URL for the repository ( For this repository: https://github.com/Jays-T/the-band-room.git ).
  2. In your local IDE open Git Bash.
  3. Change the current working directory to the location where you want the cloned directory to be made.
  4. Type git clone, and then paste the URL you copied in Step 3.
  5. The command should look like this:  git clone https://github.com/Jays-T/the-band-room.git
  6. Press enter and your local clone will be created and the response should be something like this:
> * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> * Cloning into `Spoon-Knife`...
> * remote: Counting objects: 10, done.
> * remote: Compressing objects: 100% (8/8), done.
> * remove: Total 10 (delta 1), reused 10 (delta 1)
> * Unpacking objects: 100% (10/10), done.
* For further reading and troubleshooting on cloning a repository from GitHub you can go <a href="https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository" target="_blank">here</a>.

# To preview in your browser

If you are using gitpod as your IDE:
The project runs only from the Master branch the main directory of which is:  /workspace/the-band-room
When in the main directory enter the following into the terminal command prompt
1. python3 app.py
2. This will run the contents of the directory on a local web server, on port 8080.
3. If you are working in Gitpod this will give you an option to 'open browser' which will open the default route '/the_band_room'
4. If you want to stop the local server from running, in the command prompt simply press crtl + C


# Credits

**Code**

* Thanks to <a href="https://github.com/prettyprinted" target="_blank">Anthony</a> at Pretty Printed for his <a href="https://github.com/PrettyPrinted/mongodb-user-login" target="_blank">tutorial</a> on setting up a user-registration-login system using Flask and MongoDB.

## Content

* Text on the site was written by myself

## Media

* All images sourced from <a href="https://www.coolclips.com/" target="_blank">Coolclips</a>
* Favicon and Site Logo (seen in the navbar) created with <a href="https://www.iconsflow.com/" target="_blank">Iconsflow</a>

## Acknowledgements

## Thank you to my mentor **@rheyannmagcalas_mentor** for helping me with suggestions on how to solve coding issues, reminding me to keep my plans realistic and giving great advice on potential features to add and on defensive design.
## Thank you to Niel from StudentCare at Code Institute for his advice on CRUD functionality and making sure the basics are done right.
## Thank you to h4xnoodle for your advice and consistently reminding me not to overcomplicate things. 

# FAIR-USE COPYRIGHT DISCLAIMER

* Copyright Disclaimer Under Section 107 of the Copyright Act 1976, 
 * allowance is made for "fair use" for purposes such as criticism, commenting, news reporting, teaching, scholarship, and research. 
 * Fair use is a use permitted by copyright statute that might otherwise be infringing. 
 * Non-profit, educational or personal use tips the balance in favour of fair use.

* This is for educational use.
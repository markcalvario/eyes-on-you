

What it does:
1) This web application informs undocumented immigrants of their rights by providing links and PDFs of their rights in case they come across an ICE officer.

2) Users can inform other users if there an ICE raid or checkpoint by submitting a form that gives a (1) date, (2) address, (3) and description. Although we do not currently have Firebase in our current project, we plan to implement Firebase to store user input so that we can retrieve that data and so that the python files (Data.py and Database.py) can process the data.

3) Users can access these submissions and see if ICE is near them by selecting their state that they are currently at. We plan on doing this by using Firebase.

How to use:
1) Download or clone repository
2) Open up a text editor like Visual Studio Code
3) Install virtual environment if not installed 
   a) To install do pip3 install virtualenv
   b) This should be done in the folder of this project
4) Create a virtual environment
  a) In the command line, type virtualenv (name of folder you want)
  b) Ex. virtualenv env
5) Activate virtual environment
  a) Type in your terminal: source (name of your virtualenv you created)/bin/activate
6) Install requirements like flask
  a) On terminal, type in pip3 install flask 


How we built it:
Our team used HTML as our skeleton for the foundation of our website where we were able to express most of our information through it. Our team used CSS and JavaScript to efficiently design a user-friendly website that would appear easy to navigate. We used Python to build the database in which we are able to read and analyze the information that is being stored. Github allowed us to use a common platform to build or code in real-time to see what the experimental webpage would look like.

Main Programs Used: Flask Python HTML CSS JavaScript

Challenges we ran into:
A challenge that we ran into was that we had the python code that works but had a hard time connecting our python code to our HTML code in Flask to output the ICE reports that users can report. We wanted to save the user input and display out into the section where a user can select their state so that they can see if a person reported an ICE sighting in that state. Before this hackathon, we had no prior knowledge of how to use a database platform like Firebase to store data until the last day which unfortunately we were not able to do in time.

Accomplishments that my team and I are proud of:
We are proud of how we designed our website, to be able to understand how our application may fix the implications of ICE and the dangers of interactions with them, and at least storing data into the local memory and display it even though it does not stay there when the page is refreshed.

What I learned:
We all learned a lot more HTML, CSS, JavaScript, and how to use Flask to create a basic web application. We learned that we can use Firebase to store data and plan on doing that. For example, we learned how to make a smooth scroll to a section of a page using JavaScript.

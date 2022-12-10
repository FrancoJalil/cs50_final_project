# SCRAPIEST

#### Video Demo: https://youtu.be/aL20-5f4BSc

#### Description:
Application that allows you to scrape websites very easily using commands. With these commands you can scrape a website and view the output or download it.

#### Technologies used:
- Python
- Flask
- HTML
- CSS
- Javascript
- Other small libraries or packages.

## Dependencies
pip install -r requirements.txt

## Python Files
#### main.py
Here is the flask setup, the routes and the main logic of the project.
Two routes: index("/") and get_scrap("/get_scrap")
The index route just returns to the index.html template.
The get_scrap route, if is called by the get method, takes the command entered by the user and validates it. If valid, gets what the user entered and stores it in variables. Then thanks to the scrap_validate function we scrape the requested page with the information that the user entered.
We configure the content to be readable by the user and return it so that the frontend can consume it.
If there was an error in the user command or in web scraping, it returns an HTTP error.
This route makes use of the "scrap_validate" and "http_return_error" functions to abstract things away and improve code visibility.

#### helpers.py
Contains useful functions to abstract certain parts of the code from main.py
##### scrap_validate function:
It takes as arguments the user command, same command separated by words and its length.
Validate user errors.
Scrapes a web with the user's requests using the "BeautifulSoup" and "requests" libraries. 
Then returns the requested output in text.

##### http_return_error function:
It takes as arguments a string and a status code.
Return a response with a text and a status code.

## Static files
### css/style.css
Here are the responsive css styles

### img
Here are the images used by the web

### js
Here are the javascript files

#### scripts.js
Here is the client-side logic.
That the user can send an input by pressing the "Enter" or "Intro" key.
Consume with ajax through the get method of the backend api to obtain the scrape in text.
Save a list of the user's past commands so you can see them.
/export validations.
Creation of the canvas to recreate the effect of the Matrix movie.

## templates
#### index.html
Structure of the main project screen.

## Other files
#### docs.html
Here is written the documentation of the application where you can see how to use it correctly.

## ABOUT CS50
CS50 It is the perfect course to start in the world of computer science. All topics are explained from the most basic to advanced things. What I liked the most was the number of projects I did, since the modality of the course is after a class, to do one or more projects to apply what I have learned.
A great experience.

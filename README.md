# SCRAPIEST

#### Video Demo: https://youtu.be/aL20-5f4BSc

#### Description:
Application that allows you to scrape websites very easily using commands. With these commands you can scrape a website and view the output or download it.

## Dependencies
pip install -r requirements.txt

## Python Files
#### main.py
Here is the flask setup and the main logic of the project.
Two routes: index("/") and get_scrap("/get_scrap")
The index route just returns to the html template.
The get_scrap route, if is called by the get method, takes the command entered by the user and validates it. If valid, extract what the user wants to scrape into variables. Then thanks to the "BeautifulSoup" library we scrape the requested page with the information that the user entered.
Then return the output for the frontend to consume.

#### helpers.py
Contains useful functions
###### scrap_validate:
It takes as arguments the user command, same command separated by words and its length.
Validate user errors.
Scrapes a web with the user's requests and returns the requested output in text.

###### http_return_error:
It takes as arguments a string and a status code.
Return a response with a text and a status code.

## Static files
### css/style.css
Here are the responsive css styles

### img
Here are the web images

### js
Here are the javascript files

#### scripts.js
Here is the client-side logic.
That the user can send an input by pressing the "Enter" or "Intro" key.
Consume through the get method of the backend api to obtain the scrape in text.
Save a list of the user's past commands so you can see them.
/export validations.
Creation of the canvas to recreate the effect of the Matrix movie.


## Other files
#### docs.html
Here is written the documentation of the application where you can see how to use it correctly.

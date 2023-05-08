# Flask_ECommerce_API

## Installation:

To install and run the Flask app, follow these steps:

Install Python if it is not already installed. You can download Python from the official website at https://www.python.org/downloads/.

Install Flask, Flask SQLAlchemy, and Flask Marshmallow using pip. Open a terminal or command prompt and run the following command: 
`“pip install Flask Flask-SQLAlchemy Flask-Marshmallow”`
or using the provided requirements file:
`“pip install -r requirements.txt”`

Install SQLite. SQLite is a lightweight database engine that is perfect for development and testing. You can download SQLite from the official website at https://www.sqlite.org/download.html.
Unzip the contents of the directory

## Running the app:
Open a terminal or command prompt and navigate to the directory where the app.py file is located.
Enter: “flask run” or “python3 app.py” into the terminal. This will start the Flask development server and the app will be available at `http://127.0.0.1:5000`. 

Use an application like Postman or Curl (in the terminal) to send http requests. If using postman, make sure you create a new key under the “Headers” tab and set the content-type to application/json in order to send requests.
Make sure requests conform to the routes given. A route such as `http://127.0.0.1:5000/product/2` will work, but adding another slash like `http://127.0.0.1:5000/product/2/` will not work.

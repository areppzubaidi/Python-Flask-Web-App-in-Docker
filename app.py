from flask import Flask  # // Import the Flask class from the flask package

app = Flask(__name__)  # // Create a Flask app instance. __name__ helps Flask know where to look for templates, etc.

@app.route('/')  # // Define a route. When users visit the root URL '/', this function will run
def hello():  # // Define the function that runs when '/' is accessed
    return "Hello from Flask in Docker!"  # // Return a simple message that will be displayed in the browser

if __name__ == '__main__':  # // Only run this block if the script is executed directly (not imported)
    app.run(host='0.0.0.0', port=5000)  # // Start the Flask development server on port 5000 and expose to all IPs (important for Docker)


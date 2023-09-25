from app import application # Importing the application variable in the __init__.py file.

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080) # Allows you to get a a error page in your browser when you run the application with whats wrong with your code. This is set to false on the actual application.

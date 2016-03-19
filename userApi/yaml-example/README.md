Google App Engine Examples in Python

# Enforcing sign in and admin access with app.yaml

If you have pages that require the user to be signed in in order to access, you can enforce this in your app.yaml file. If a user accesses a URL configured to require sign-in and the user is not signed in, App Engine redirects the user to the appropriate Google sign-in page, then directs the user back to your app's URL after signing in or registering successfully.

##### Using pip Requirements Files

pip can read a list of libraries to install from a file, known as a requirements file. Requirements files make it easy to set up a new development environment for your app, and upgrade to new versions of libraries.

A requirements file is a text file with one line per library, listing the package name and version:

Flask==0.10

To install the libraries from a requirements file, use the -r flag in addition to the -t lib flag:

pip install --upgrade -r requirements.txt -t lib

##### Local Demo

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/yaml/devserver.png "devserver")

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/yaml/login.png "login")

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/yaml/hello.png "hello")
Google App Engine Examples in Python

# User authentication in Python

The following example greets a user who has signed in to the app with a personalized message and a link to sign out. If the user is not signed in, the app offers a link to the sign-in page for Google Accounts.

##### Using pip Requirements Files

pip can read a list of libraries to install from a file, known as a requirements file. Requirements files make it easy to set up a new development environment for your app, and upgrade to new versions of libraries.

A requirements file is a text file with one line per library, listing the package name and version:

Flask==0.10

To install the libraries from a requirements file, use the -r flag in addition to the -t lib flag:

pip install --upgrade -r requirements.txt -t lib

##### Local Demo

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/auth/devserver.png "devserver")

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/auth/login.png "login")

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/yaml/login.png "login")

![alt text](https://storage.googleapis.com/ymedlop-sandbox.appspot.com/examples/gae/userApi/auth/logon.png "hello")

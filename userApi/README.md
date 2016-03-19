Google App Engine Examples in Python

# userApi Examples
App Engine applications can authenticate users using one of these methods: Google Accounts or accounts on your own Google Apps domains. An application can detect whether the current user has signed in, and can redirect the user to the appropriate sign-in page to sign in or, if your app uses Google Accounts authentication, create a new account. While a user is signed in to the application, the app can access the user's email address , as well as a unique user ID. The app can also detect whether the current user is an administrator, making it easy to implement admin-only areas of the app.

from https://cloud.google.com/appengine/docs/python/users/
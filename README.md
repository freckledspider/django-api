# General Assembly Coursework - Django/Python Building and Deploying an API

### Learning Objectives
- Creating an API
- Setting Cors Headers
- Testing an API
- Deploying an API

### Django REST Framework
When creating an API previously we did without any external help and making basic crud routes ended being a bit tedious...

- write all crud functions individually
- we had to convert our data to json then back to a dictionary to send back as json
- the shape of the data isn't we would traditionally would expect
- we had to turn off CSRF security and other security features to make work

DjangoRestFramework fixes all the above and creates a nice abstraction for creating REST API's with django. Let's do it!

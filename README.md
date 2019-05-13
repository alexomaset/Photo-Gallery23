# Photo-Gallery Application

## Author
[Alex Omaset]()

## Description
Photo-Gallery is a django application that allows a user/client to view different categories of photos. When the user clicks on a single photo the image is expanded enabling the user to view details of the photo eg Name of the image, category and location. A user can also search photos using different categories eg Nature,Technology,Vacation,Sports,Music etc.Finally the user can filter photos based on the location.
## Behaviour Driven Development

| Behaviour                                                                                 | Input                                                     | Output                                                                            |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------|
| User view various photos on homepage                                                      | On page load                                              | Display various categories of photos                                              |
| A single image appears on a modal                                                         | User clicks on a single image                             | A single modal image appears on top of other images displaying image descriptions |
| Filters all images on a specific category                                                 | User searches images based on categories                  | All images based on that category all displayed on a different template           |
| All images of different categories but the same location are displayed                    | User clicks on the dropdown menu with different locations | A page with images of a particular location appear                                |
| The program should navigate home page when the app name/Home Tag is clicked on the navbar | Click on Pic-Galore/Home Tag  on the navigation bar       | Redirect to the Home page                                                         |
### Project Setup instructions
Use the following commands to use this project.
- git clone `https://github.com/alexomaset/Photo-Gallery23.git`
- install `python 3.6`
- Install [Postgresql](https://www.postgresql.org/download/)
- cd Blog-It
- Navigate to the virtual environment using `source virtual/bin/activate`
- `atom .`  //For those using atom text editor.
- `code .`  //For those using Visual Studio editor.


### Install dependancies
Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`

### Create the Database
```
psql
CREATE DATABASE <preferred name>;
```
- Run `python3.6 manage.py runserver`
- Access the application on this localhost address `http://127.0.0.1:8000`

### Technologies used
The different technologies that were used to develop this program include:
```
1. Python 3.6 
2. Bootstrap
3. HTML
4. CSS
5. Postgresql
6. MDBootstrap
7. Django Framework
```

### Link to live site
Here is a link to the live site 
### Contact Me
If you have any suggestions, additions or modifications on this project you can reach me via my email: alexomaset711@gmail.com

### License  & Copyright information
Copyright (c) 2019 Alex Omaset

[MIT License](./LICENSE)
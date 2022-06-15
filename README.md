<h1 align= "center" dir="auto"> Welcome to <a href="https://chefs-book-app.herokuapp.com/">Chef's Book</a>! </h1> <a name="top"> </a>
</br>
</br>
<h5 align= "center" dir="auto">
   <a href="https://esena.herokuapp.com/">» Live Link «</a>
</h5>
<h4 align= "center" dir="auto">
  <a href="https://github.com/lanakomar/Chefs-book/wiki">» Explore the Wiki «</a>
</h4>
Chef's book is a food-focused web apllication inspired by [NYTCooking](https://cooking.nytimes.com/). The recipes on the website are posted by members of the Chef's Book community.  Members of the community can also customize theri owm Grocery list so they could easily shop for the required items for their next culinary adventure.

# Technologies Used
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
</br>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

# Features
### Home Page
Users can scroll through the existing recipes, as well as log into an existing account, sign up or test the site by clicking on the Demo User feature to explore the app.

### Navigation
* The navigation bar is displayed on the top of the page and persists on each page.
Once the user is logged in, they can open detailed description of every recipe, create their own recipes and store them in the recipe box.

### Notes
* Notes section is displayed on the recipe page. Logged in user can easily read through the notes left by other members of the community, as well as create their own notes on every recipe.

### Grocery List
* Logged in user can add recipe ingredients to their own grocery list. User can easily modify the existing list by removing separate items or delelting the required ingredients for the whole recipe.

# Getting started
1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/lanakomar/Chefs-book.git
   ```

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** and **.flaskenv** files based on the examples with proper settings for your
   development environment

4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, cd into [react-app](./react-app/), run npm install to install dependencies. Run this application from this location using `npm start`.

***


*IMPORTANT!*
   psycopg2-binary MUST remain a dev dependency because you can't install it on alpine-linux.
   There is a layer in the Dockerfile that will install psycopg2 (not binary) for us.
***

### Dev Containers (OPTIONAL for M1 Users)
The following instructions detail an *optional* development setup for M1 Mac users having issues with the `psycopg` package.

1. Make sure you have the [Microsoft Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.
2. Make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed on your computer.
3. Clone the repository (only this branch)
   ```bash
   git clone [https://github.com/appacademy-starters/python-project-starter.git](https://github.com/lanakomar/Chefs-book.git)
   ```
4. Open the repo in VS Code.
5. Click "Open in Container" when VS Code prompts to open container in the bottom right hand corner.
6. **Be Patient!** The initial install will take a LONG time, it's building a container that has postgres preconfigured and even installing all your project dependencies. (For both flask and react!)

   **Note:** This will take much less time on future starts because everything will be cached.

7. Once everything is up, be sure to make a `.env` and `.flaskenv` files based on `.env.example`/`.flaskenv.example` in both the root directory and the *react-app* directory before running your app. You do not need a `DATABASE_URL` in the `.env` file if you are using this Docker setup for development - the URL is already set in the image (see `.devcontainer/Dockerfile` for the URL).

8. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```



<br>

## Helpful commands
|    Command            |    Purpose    |
| -------------         | ------------- |
| `pipenv shell`        | Open your terminal in the virtual environment and be able to run flask commands without a prefix |
| `pipenv run`          | Run a command from the context of the virtual environment without actually entering into it. You can use this as a prefix for flask commands  |
| `flask db upgrade`    | Check in with the database and run any needed migrations  |
| `flask db downgrade`  | Check in with the database and revert any needed migrations  |
| `flask seed all`      | Just a helpful syntax to run queries against the db to seed data. See the **app/seeds** folder for reference and more details |
| `flask seed undo`     | Just a helpful syntax to run queries against the db to delete seed data. See the **app/seeds** folder for reference and more details |

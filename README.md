# Team 085 Group A Backend Application

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f942cbe941324a0db0b4079cebb193a0)](https://app.codacy.com/gh/BuildForSDGCohort2/Team-085-Backend?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDGCohort2/team-085-group-a-backend&utm_campaign=Badge_Grade_Settings)

Team 085 Group A Backend Application

## Application Stack

The Application Tech Stack includes:
-   A code editor you're comfortable with. I suggest [Visual Studio Code](https://code.visualstudio.com/) or [SublimeText](https://www.sublimetext.com/).
-   **Git**: The [Version Control](https://git-scm.com/downloads) manager of choice.
-   **Python3**: The [server language](https://www.python.org/downloads/)
-   **Flask**: [Server Framework](https://flask.palletsprojects.com/en/1.1.x/)
-   **PostgreSQL**: [Database](https://www.postgresql.org/) of choice
-   **SQLAlchemy**: [ORM of choice](https://www.sqlalchemy.org/) to communicate between the python server and the Postgres Database. [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) is directly used.
-   **Heroku**: [Deployment Platform](https://www.heroku.com/)
-   **[Postman](https://www.postman.com/)**: Testing the Application Endpoints

## Working with the application locally
Make sure you have [Python](https://www.python.org/downloads/) installed.

1.  **Fork the Repository**<br>

2.  **Clone the Repository**<br>
    Replace `<your-username>` with your github username.
    ```bash
    git clone -b master https://github.com/<your-username>/fsnd-capstone.git
    ```

3.  **Set up a virtual environment**:<br>
    ```bash
    virtualenv env
    source env/Scripts/activate # for windows
    source env/bin/activate # for MacOs
    ```
    > If you don't have `virtualenv` installed, run **Step 3** first. Virtualenv has been included in the requirements.txt file. Then proceed to run **Step 2** again.

4.  **Install Dependencies**:<br>
    ```bash
    pip install -r requirements.txt
    ```

5.  **Export Environment Variables**<br>
        Refer to the `setup.sh` file and export the environment variables for the project.

6.  **Create Local Database**:<br>
        Create a local database and export the database URI as an environment variable with the key `DATABASE_PATH`.

7.  **Run Database Migrations**:<br>
    ```bash
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
    ```

8.  **Run the Flask Application locally**:<br>
    ```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run
    ```

9.  See the [CONTRIBUTING](CONTRIBUTING.md) to see how to make contributions.

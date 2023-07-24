# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy

FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface.

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.



### How to run the REST API
Get this project from Github

```shell
    git clone https://github.com/emilianstoyanov/REST-API-with-FastAPI-SQLAlchemy-PostgreSQL.git
 ```

Setting up the database

* Install PostgreSQL and create your user and database

* Change this line in database.py to

```shell
engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
```

### Create a virtual environment
This can be done with ```python -m venv env```

activate the virtual environment with

```shell
env/bin/activate
```
or
```shell
env\Scripts\activate
```
### Install the requirements
```shell
pip install -r requirements.txt
```
### Create the database
```shell
python create_db.py
```
### Run the API
```shell
python main.py
```
<!-- ```shell        
uvicorn main:app --reload
 ``` -->

### http://localhost:8000/docs

 ![Alt text](image.png)



### http://localhost:8000/redoc

![Alt text](image-1.png)


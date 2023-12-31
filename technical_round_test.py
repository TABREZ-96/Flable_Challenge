##### Python Data Manipulation ####


# Question: Given a list of integers, write a Python function that finds all even numbers in the list and squares them. The result should be a new list containing the squared even numbers in the order they appeared in the original list.
def square_even_numbers(numbers: list) -> list:
    pass # Your implementation here
# Expected Output: For the list [1, 2, 3, 4, 5, 6], the function should return [4, 16, 36].


#### Fast API Implementation ####
# Question: Implement a FastAPI application with an endpoint `/analyze/{text}` that takes a text string as a path parameter and returns the number of vowels, consonants, and words in the text.
from fastapi import FastAPI

app = FastAPI()

@app.get("/analyze/{text}")
def analyze_text(text: str):
    pass  # Your implementation here

# Expected Output: For a request to `/analyze/hello world`, the API should return {"vowels": 3, "consonants": 5, "words": 2}.


#### Database Queries - Postgres ####
# DB connection details proided in db_lib
# Question: Given a PostgreSQL database with a table named `products` having columns `id`, `name`, `price`, and `category`, write a Python function using the `psycopg2` library to retrieve the most expensive product in each category. Use the provided hostname, server credentials, and dbname.
import psycopg2

def get_most_expensive_products(hostname, user, password, dbname) -> list:
    pass  # Your implementation here

# Expected Output: The function might return [{'category': 'Electronics', 'name': 'Laptop', 'price': 1200}, {'category': 'Books', 'name': 'Special Edition', 'price': 150}].



#### FAST API wiht Postgres ####
# Question: Extend the FastAPI application to include an endpoint `/products/top` that connects to the PostgreSQL database and returns the most expensive product in each category. Use the provided hostname, server credentials, and dbname.
@app.get("/products/top")
def get_top_products():
    pass  # Your implementation here

# Expected Output: For a request to `/products/top`, the API might return [{'category': 'Electronics', 'name': 'Laptop', 'price': 1200}, {'category': 'Books', 'name': 'Special Edition', 'price': 150}].




#### ERROR Handeling ####
# Question: Enhance the FastAPI application to handle potential errors robustly. Specifically, for the `/analyze/{text}` endpoint, ensure it can handle non-English characters gracefully and provide a meaningful error message if the text contains any numeric characters.
@app.get("/analyze/{text}")
def analyze_text(text: str):
    pass  # Your implementation here

# Expected Output: For a request to `/analyze/h3llo`, the API should return a 400 Bad Request with a message `Text should not contain numeric characters`.


#### Segmentation using AI ####
# Question: Use the Kaggle titanic dataset (https://www.kaggle.com/competitions/titanic/data) to divide the data points into multiple segments such that the model is able to classify a new entry into various segments.
E.g. Segment/ Cluster 1: Based on a person surviving (survival = 1) and different ticket class "pclass" (3 clusters which segments all survivors based on their ticket class)
Segment/ Cluster 2: A person bought a second class ticket and is a female, based port "embarked" they embarked on (3 clusters for all female passengers who bought a second class ticket, based on the port of embarking)
Segment/ Cluster 3: Based on sex and age range of people cluster them into different groups age ranges (0-10: Kids, 10-20: Teens, 20-30: Young, 30-50: Middle Age, 50+: Senior)

Also create some segments on your end to show correlation between different features of the dataset.


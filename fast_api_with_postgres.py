from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

class Posgresdbsetup():
    def __init__(self, conndet):
        self.p_con = 'dbname={dbname} user={user} password={password} host={host} port={port}'\
                        .format(dbname=conndet["pgdbname"], user=conndet["pguser"],
                                password=conndet["pgpass"], host=conndet["pghost"],
                                port=conndet["pgport"])
        self.conn = psycopg2.connect(self.p_con)
        self.cursor = self.conn.cursor()

@app.get("/products/top")
def get_top_products():
    # Connect to the database
    hostname, user, password, dbname = "85.214.66.84", "test_user", "testpass", "public"
    conndet = {"pgdbname": dbname, "pguser": user, "pgpass": password, "pghost": hostname, "pgport": 3100}
    db = Posgresdbsetup(conndet)

    try:
        # The SQL query to retrieve the most expensive product in each category
        query = '''
                SELECT DISTINCT ON (category) category, name, price
                FROM products
                ORDER BY category, price DESC;
                '''

        # Execute the query
        db.cursor.execute(query)

        # Fetch all the results
        result = db.cursor.fetchall()

        # Convert the result from a list of tuples to a list of dictionaries
        formatted_result = [{'category': row[0], 'name': row[1], 'price': float(row[2])} for row in result]

        return formatted_result
    except Exception as e:
        # Log the exception
        print(f"Exception: {str(e)}")
        # Raise a custom HTTPException with a 500 status code
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        # Close the cursor and connection
        db.cursor.close()
        db.conn.close()

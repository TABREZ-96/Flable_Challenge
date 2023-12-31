import psycopg2

class Posgresdbsetup():
    def __init__(self, conndet):
        self.p_con = 'dbname={dbname} user={user} password={password} host={host} port={port}'\
                        .format(dbname=conndet["pgdbname"], user=conndet["pguser"],
                                password=conndet["pgpass"], host=conndet["pghost"],
                                port=conndet["pgport"])
        self.conn = psycopg2.connect(self.p_con)
        self.cursor = self.conn.cursor()

def get_most_expensive_products(conndet) -> list:
    db_setup = Posgresdbsetup(conndet)

    b_setup = Posgresdbsetup(conndet)
    
    sql_query = """
        SELECT category, MAX(price) AS max_price
        FROM products
        GROUP BY category;
    """
    
    db_setup.cursor.execute(sql_query)
    
    products = db_setup.cursor.fetchall()
    
    db_setup.cursor.close()
    db_setup.conn.close()
    
    return products

hostname, user, password, dbname = "85.214.66.84", "test_user", "testpass", "public"
conndet = {"pgdbname": dbname, "pguser": user, "pgpass": password, "pghost": hostname, "pgport": 3100}

most_expensive_products = get_most_expensive_products(conndet)

print(most_expensive_products)
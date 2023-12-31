import psycopg2

class Posgresdbsetup():
    def __init__(self, conndet):
        self.p_con = 'dbname={dbname} user={user} password={password} host={host} port={port}'\
                        .format(dbname = conndet["pgdbname"], user = conndet["pguser"],
                                password = conndet["pgpass"], host = conndet["pghost"],
                                port = conndet["pgport"])
        self.conn = psycopg2.connect(self.p_con)
        self.cursor = self.conn.cursor()

def get_most_expensive_products(conndet) -> list:
    db = Posgresdbsetup(conndet)
    query = '''
            SELECT DISTINCT ON (category) category, name, price
            FROM products
            ORDER BY category, price DESC;
            '''
    db.cursor.execute(query)
    result = db.cursor.fetchall()
    db.cursor.close()
    db.conn.close()

    formatted_result = [{'category': row[0], 'name': row[1], 'price': float(row[2])} for row in result]

    return formatted_result

hostname, user, password, dbname = "85.214.66.84", "test_user", "testpass", "public"
conndet = {"pgdbname": dbname, "pguser": user, "pgpass": password, "pghost": hostname, "pgport": 3100}

result = get_most_expensive_products(conndet)
print(result)

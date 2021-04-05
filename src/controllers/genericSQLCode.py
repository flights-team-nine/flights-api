def setup_db():
    conn = mysql.connector.connect(
        host="ipofexternal, or in our case 127.0.0.1",
        user= "root",
        passwd="",
        database="honorflightwhatever",

    )
    if conn.is_connected():
        return conn

    print("Unable to establish a connection to the database.")
    return None


def sample_db_input(conn, sql, values):
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()


def sample_db_output(conn, sql, values):
    cursor = conn.cursor()
    cursor.execute(sql, values)
    results = cursor.fetchall()
    return results


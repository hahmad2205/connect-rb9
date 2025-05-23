import pyodbc

# Define connection parameters
server = ""
database = "master"
username = ""
password = ""

# Create the connection string
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"UID={username};"
    f"PWD={password};"
    f"DATABASE={database};"
)

# Connect and run a test query
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    print("Connection established")
    for row in cursor.fetchall():
        print("DB Name:", row.name)
    conn.close()
except Exception as e:
    print("Connection failed:", e)

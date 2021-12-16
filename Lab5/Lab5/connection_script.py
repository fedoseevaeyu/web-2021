import pyodbc

connectionString = ("Driver={SQL Server Native Client 11.0};"
                    "Server=localhost\\SQLEXPRESS;"
                    "Database=Applications;"
                    "Trusted_Connection=yes;")    

request1 = """  INSERT INTO dbo.Prog_language 
                SELECT 'C++', 'C++ is the best programming language!', 1983 
                UNION ALL 
                SELECT 'Python', 'Python is often ised for machine learning.', 1991 """

request2 = "SELECT * FROM dbo.Prog_language"

connection = pyodbc.connect(connectionString, autocommit=True)
dbCursor = connection.cursor()
dbCursor.execute(request1)
dbCursor.execute(request2)
for row in dbCursor:
    print(f"{row.ID_language} {row.Language_name} {row.Descript} {row.Creation_year}")
connection.commit()
dbCursor.close()
connection.close()

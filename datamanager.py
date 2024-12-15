import sqlite3


class DBMmanager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Projekts(
                id INT PRIMARY KEY,
                title VARCHAR(255),
                image TEXT,
                description TEXT
            );

        """)


        self.connection.commit()

    def addd_projeckt(self, id, title, image, description):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Projekts(id , title, image , description) VALUES (? , ? , ? , ?) ", [id, title, image , description])
        self.connection.commit()
        cursor.close()

    def get_projeckts(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Projekts")
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_projeckts2(self , poj_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Projekts WHERE poj_id = ?" , [poj_id])
        res = cursor.fetchall()
        cursor.close()
        return res

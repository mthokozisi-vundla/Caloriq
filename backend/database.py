import pymysql


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="@Omphile01112",
        database="caloriq"
    )




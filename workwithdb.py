from datamanager import DBMmanager

db_manager = DBMmanager("Projects.db")
db_manager.create_tables()

db_manager.addd_projeckt(0 , "Тестовий проєкт" , "ДІАГРАМИ_3psd.jpg" , "тестовий проєкт")
import mysql.connector as sql
import pandas as pd

mydb = sql.connect(
    host='localhost',
    user='root',
    password='sethvolson333.',
    database="college"
)

data = "SELECT * FROM student"

df = pd.read_sql_query( data , mydb)

mean = df.mean(axis = 'columns')

df['Average'] = mean.round(1)

df['Grade'] = pd.cut(df['Average'],bins=[0, 39.9, 49.9 , 59.9 , 69.9 , 79.9, 100 ],
                     labels= ['F', 'E', 'D', 'C', 'B', 'A'])

copy_list = ['Firstname', 'Surname' , 'Average' , "Grade"]
dffinal= df[copy_list].copy()

print(dffinal)

dffinal.to_sql(
    name = 'grades',
    con = mydb,
    if_exists = 'append',
    index = False
)




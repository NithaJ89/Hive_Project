from connection import hiveConnection

def insert_data(filename,tablename):
    try:
        c = hiveConnection()
        d = f"""
            load data local inpath '/home/nitha/PycharmProjects/PythonProject/Bigdata91/hive_project/data/{filename}' overwrite into table {tablename}
            """
        c.execute(d)
        print(f'{filename} inserted to table "{tablename}" Successfully...')

    except Exception as e:
        print(f'Error in table creation of: {tablename} ', e)

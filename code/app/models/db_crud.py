from dotenv import load_dotenv
import os
load_dotenv('./.env')
sql_username=os.environ.get("sql_username")
sql_password=os.environ.get('sql_password')
sql_main_database=os.environ.get('sql_main_database')
sql_hostname=os.environ.get('sql_hostname')
sql_port=os.environ.get('sql_port')
db_url = f"mysql+pymysql://{sql_username}:{sql_password}@{sql_hostname}:{sql_port}/{sql_main_database}"

class db_crud:

    @staticmethod
    def runQuery(query):
        from sqlalchemy import create_engine, text
        from sqlalchemy.orm import sessionmaker
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.execute(text(query))
        rows = result.fetchall()
        session.close()
        return rows

    @staticmethod
    def getHolder(address):
        query = f'''
        SELECT address,count FROM wallet_hold_token WHERE contractAddress = {address}
            '''
        
        return db_crud.runQuery(query)

from dotenv import load_dotenv
import os
load_dotenv('./.env')
sql_username=os.environ.get("sql_username")
sql_password=os.environ.get('sql_password')
sql_main_database=os.environ.get('sql_main_database')
sql_hostname=os.environ.get('sql_hostname')
sql_port=os.environ.get('sql_port')
db_url = f"mysql+pymysql://{sql_username}:{sql_password}@{sql_hostname}:{sql_port}/{sql_main_database}"

class db_init:
    @staticmethod
    def create_db():

        from sqlalchemy import create_engine, text
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy import create_engine

        # Step 1: Create a database engine
        engine = create_engine(db_url)

        # Step 2: Define individual CREATE TABLE statements
        create_table_statements = [
            '''
            CREATE TABLE token (
                contractAddress VARCHAR(255) PRIMARY KEY,
                totalSupply DECIMAL(38, 18),
                symbol VARCHAR(10),
                transferTax DECIMAL(5, 2),
                sellTax DECIMAL(5, 2),
                buyTax DECIMAL(5, 2),
                decimals INT
            )
            ''',
            '''
            CREATE TABLE walletAddress (
                address VARCHAR(255) PRIMARY KEY
            )
            ''',
            '''
            CREATE TABLE wallet_hold_token (
                contractAddress VARCHAR(255),
                address VARCHAR(255),
                count DECIMAL(38, 18),
                PRIMARY KEY (contractAddress, address),
                FOREIGN KEY (contractAddress) REFERENCES token(contractAddress),
                FOREIGN KEY (address) REFERENCES walletAddress(address)
            )
            ''',
            '''
            CREATE TABLE events (
                txnHash VARCHAR(66),
                logIndex INTEGER,
                data VARCHAR(255),
                address VARCHAR(255),
                input VARCHAR(255),
                `from` VARCHAR(255),
                `to` VARCHAR(255),
                block INTEGER,
                PRIMARY KEY (txnHash, logIndex),
                FOREIGN KEY (address) REFERENCES token(contractAddress)
            )
            ''',
            '''
            CREATE TABLE topics (
                txnHash VARCHAR(66),
                logIndex INTEGER,
                topic VARCHAR(255),
                PRIMARY KEY (txnHash, logIndex, topic)
            )
            '''
        ]

        # Step 3: Execute the CREATE TABLE statements
        with engine.connect() as connection:
            for statement in create_table_statements:
                connection.execute(text(statement))

        return {"message": "Database created successfully"}
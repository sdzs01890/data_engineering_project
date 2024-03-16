from extract import extract_data
from transform import transform_data
from sqlalchemy import create_engine

# ## Load
# Load data into Postgres database

def load_data(df):
    # postgres configuration
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = '172.18.0.3'
    DB_PORT = '5432'
    DB_NAME = 'TMDB_API'

    # Create a connection string for SQLAlchemy
    connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
    
    df.to_sql('movies', engine, if_exists='replace', index=False)

def main():
    api_key = "9933bd975aa94593210a60b87ca357df" 
    
    print("extracting data...")
    data = extract_data(api_key)

    print("transforming data...")
    transformed_data = transform_data(data)

    print("loading data...")
    load_data(transformed_data)
    
    print("Finished.")

if __name__ == "__main__":
    main()
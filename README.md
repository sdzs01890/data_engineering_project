## Overview
This is an engineer case study to perform an ETL process so that the data can be used by data analysts or data scientists. The project include these tech:

1. Python programming language
2. Docker
3. PostgreSQL

## ETL (Extract, Transform and Load)
1. Extract:
I extracted the data from TMDB website using API, sorted by the most popular ones. The number of extracted rows is defined by a parameter called "nb_page_to_load".

2. Transform:
In this stage, I used python to clean and transform the data. This mainly includes two steps:
Exclude the unnecessary columns
Deleted the rows with null values

3. Load:
Finally, the data is loaded as table to PostgreSQL database in Docker container.

## How to use

1. Clone this repository
2. Run docker compose up -d to execute the program
3. Go to localhost:8080 to access pgadmin
   id: admin@admin.com
   password: root
![image](https://github.com/sdzs01890/data_engineering_project/assets/78092716/eaea7d3d-df21-4a6d-bd1d-2baf45b58247)

4. Once you are connected, click “Add new server" and configure the PostgreSQL database. You can find the IP address to connect using "docker inspect [Your Postgres Container ID]
![image](https://github.com/sdzs01890/data_engineering_project/assets/78092716/8b4d7076-4869-4c94-87ce-6ad998edf61f)

5. Now, you can visualize the tables in pgadmin4 and ETL process is completed!

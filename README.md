Overview
This is an engineer case study to perform an ETL process so that the data can be used by data analysts or data scientists. The project include these tech:

Python programming language
Docker
PostgreSQL

ETL (Extract, Transfrom and Load)
Extract:
I extracted the data from TMDB website using API, sorted by the most popular ones. The number of extracted rows is defined by a parameter called "nb_page_to_load".

Transform:
In this stage, I used python to clean and transform the data. This mainly includes two steps:
Exclude the unnecessary columns
Deleted therows with null values

Load:
Finally, the data is loaded as table to postgreSQL database in docker cointainer.

How to use
1. Clone this repository
2. Run docker compose up -d to execute the program
3. Go to localhost:8080 to access pdamin
   id: admin@admin.com
   password: root
![image](https://github.com/sdzs01890/data_engineering_project/assets/78092716/eaea7d3d-df21-4a6d-bd1d-2baf45b58247)

5. Once you are connected, enter the postgres configuration to visualise the tables

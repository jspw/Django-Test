### Install Postgresql : 
- `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib`

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks:


- `sudo su -postgres`

- `sudo -u postgres psql`       
- Create Database `CREATE DATABASE myproject;`
- connect to database : `\c myproject`
- Find port : `sudo netstat -plunt |grep postgres`


### Install postgresql in django 
- `pip install psycopg2`

error : 

        `psql: error: could not connect to server: could not connect to server: No such file or directory
        Is the server running locally and accepting
        connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?` 


#### Solution
- `sudo systemctl start postgresql@12-main`   **9.5 is my postgesql version**

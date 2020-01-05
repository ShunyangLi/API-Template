-- the init file of database

-- this is the user's table
-- role contain whether admin or customer
-- status is checking whether activate
CREATE TABLE IF NOT EXISTS User(
    username TEXT PRIMARY KEY ,
    password TEXT NOT NULL ,
    email TEXT ,
    role TEXT NOT NULL ,
    status TEXT NOT NULL ,
    token TEXT
);
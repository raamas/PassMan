/*passwords*/
DROP TABLE password;
CREATE TABLE passwords (
    id  INTEGER PRIMARY KEY,
    site TEXT,
    email TEXT,
    password TEXT
);
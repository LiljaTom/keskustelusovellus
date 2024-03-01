DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS groups CASCADE;
DROP TABLE IF EXISTS threads CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS threadlikes CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    content TEXT,
    group_id INTEGER REFERENCES groups,
    title TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    thread_id INTEGER REFERENCES threads,
    user_id INTEGER REFERENCES users
);

CREATE TABLE threadlikes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads
);

--INSERT INTO users (username, password) VALUES ('username', 'password')
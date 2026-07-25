

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    hashed_pass VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS classes (
    id SERIAL PRIMARY KEY,
    class_name VARCHAR(50) NOT NULL,
    class_desc VARCHAR,
    hpd INTEGER NOT NULL,
    skill_pool VARCHAR(255) NOT NULL, -- FIX TO REFERENCE A TABLE OF SKILLS LATER
    num_skills INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS class_features (
    id SERIAL PRIMARY KEY,
    class_id INTEGER REFERENCES classes(id),
    feature_name VARCHAR(100) NOT NULL,
    feature_description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS proficiencies (
    id SERIAL PRIMARY KEY,
    prof_name VARCHAR(100) NOT NULL,
    prof_desc TEXT NOT NULL,
    prof_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS characters (

    id SERIAL PRIMARY KEY,
    users_id INTEGER REFERENCES users(id),
    char_name VARCHAR(50) NOT NULL,
    char_level INTEGER NOT NULL,
    proficiency_bonus INTEGER NOT NULL,
    char_class INTEGER REFERENCES classes(id)
);

CREATE TABLE IF NOT EXISTS character_profs (
    id SERIAL PRIMARY KEY,
    character_id INTEGER REFERENCES characters(id),
    prof_id INTEGER REFERENCES proficiencies(id)
);
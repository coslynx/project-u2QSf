CREATE TABLE trainers (
    id INTEGER PRIMARY KEY,
    discord_id TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL,
    experience INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    trainer_id INTEGER,
    name TEXT NOT NULL,
    level INTEGER DEFAULT 1,
    experience INTEGER DEFAULT 0,
    FOREIGN KEY (trainer_id) REFERENCES trainers(id)
);

CREATE TABLE gyms (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    leader_id INTEGER,
    badge_name TEXT,
    FOREIGN KEY (leader_id) REFERENCES trainers(id)
);

CREATE TABLE tournaments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    prize TEXT,
    start_date TEXT,
    end_date TEXT
);

CREATE TABLE trades (
    id INTEGER PRIMARY KEY,
    trainer1_id INTEGER,
    trainer2_id INTEGER,
    pokemon1_id INTEGER,
    pokemon2_id INTEGER,
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (trainer1_id) REFERENCES trainers(id),
    FOREIGN KEY (trainer2_id) REFERENCES trainers(id),
    FOREIGN KEY (pokemon1_id) REFERENCES pokemon(id),
    FOREIGN KEY (pokemon2_id) REFERENCES pokemon(id)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    date TEXT
);

CREATE TABLE badges (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    image_url TEXT
);

CREATE TABLE outfits (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT,
    price INTEGER
);

CREATE TABLE storage (
    id INTEGER PRIMARY KEY,
    trainer_id INTEGER,
    pokemon_id INTEGER,
    FOREIGN KEY (trainer_id) REFERENCES trainers(id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);

CREATE TABLE login_bonus (
    id INTEGER PRIMARY KEY,
    trainer_id INTEGER,
    last_login_date TEXT,
    bonus_received BOOLEAN DEFAULT 0,
    FOREIGN KEY (trainer_id) REFERENCES trainers(id)
);

CREATE TABLE marketplace (
    id INTEGER PRIMARY KEY,
    pokemon_id INTEGER,
    price INTEGER,
    for_sale BOOLEAN DEFAULT 1,
    FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
);
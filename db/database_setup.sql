CREATE TABLE queue_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uri TEXT NOT NULL,
    method TEXT NOT NULL,
    params TEXT,
    headers TEXT,
    processed BOOLEAN DEFAULT 0
);

CREATE TABLE queue_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    status_code INTEGER NOT NULL,
    body TEXT,
    FOREIGN KEY (request_id) REFERENCES queue_requests (id)
);

INSERT INTO queue_requests (uri, method, params, headers) VALUES
('/wiki/Python_(programming_language)', 'GET', '{}', '{}'),
('/wiki/JavaScript', 'GET', '{}', '{}'),
('/wiki/Main_Page', 'GET', '{}', '{}'),
('/wiki/Hydrostatic_equilibrium', 'GET', '{}', '{}')
CREATE DATABASE IF NOT EXISTS contact_center;

USE contact_center;

CREATE TABLE calls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    call_id VARCHAR(50),
    direction ENUM('inbound', 'outbound', 'missed') NOT NULL,
    from_number VARCHAR(20),
    to_number VARCHAR(20),
    agent_name VARCHAR(100),
    start_time DATETIME,
    duration INT,
    transcription TEXT,
    summary TEXT,
    recording_url VARCHAR(255),
    freshdesk_contact_id INT,
    freshdesk_ticket_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    mobile VARCHAR(20),
    job_title VARCHAR(100),
    company VARCHAR(100),
    freshdesk_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

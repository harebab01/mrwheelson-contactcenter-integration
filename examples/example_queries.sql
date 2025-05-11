-- Zoek alle inbound calls van een nummer
SELECT * FROM calls WHERE from_number = '+31612345678' AND direction = 'inbound';

-- Zoek laatste 10 gesprekken
SELECT * FROM calls ORDER BY start_time DESC LIMIT 10;
-- Keep a log of any SQL queries you execute as you solve the mystery.
-- description of the crime
SELECT description
FROM crime_scene_reports
WHERE month = 7 and day = 28 and year = 2021 and description = "Humphrey Street";

--
SELECT transcript
FROM interviews
WHERE month = 7 and day = 28 and year = 2021 and transcript like "%bakery%";

-- the main block: car exit from the parking && atm trans && caller short call && passenger in the flight
SELECT people.id, people.name
FROM bakery_security_logs, people
WHERE bakery_security_logs.activity = "exit" and bakery_security_logs.license_plate = people.license_plate and month = 7 and day = 28 and year = 2021 and hour = 10 and minute between 15 and 25

INTERSECT

SELECT p.id, p.name
FROM bank_accounts as b, atm_transactions as t, people as p
WHERE b.account_number = t.account_number and t.atm_location like "%Leggett Street%" and t.month = 7 and t.day = 28 and p.id = b.person_id

INTERSECT

SELECT p1.id, p1.name
FROM phone_calls, people as p1
WHERE duration< 60 and month = 7 and day = 28 and year = 2021 and caller = p1.phone_number

INTERSECT

SELECT people.id, people.name
FROM flights, people, passengers
WHERE passengers.flight_id = flights.id and  flights.id = 36 and people.passport_number = passengers.passport_number;

-- reciever - the helper
SELECT p1.name as caller, p2.name as receiver
FROM phone_calls, people as p1, people as p2
WHERE duration< 60 and month = 7 and day = 28 and year = 2021 and caller = p1.phone_number and receiver = p2.phone_number;

-- first flight from fiftyville
SELECT flights.id, dest_p.city
FROM flights, airports as org_p, airports as dest_p
WHERE month = 7 and day = 29 and year = 2021 and org_p.city = "Fiftyville" and flights.origin_airport_id = org_p.id and flights.destination_airport_id = dest_p.id
ORDER BY flights.hour, flights.minute
LIMIT 1;




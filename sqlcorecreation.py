import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.dialects.postgresql import JSONB

from sqlalchemy import MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/demo"

from sqlalchemy import (
    Table,
    Column,
    Integer,
    Text,
    CHAR,
    CheckConstraint,
    VARCHAR,
    TIMESTAMP,
    NUMERIC,
    Index,
    ForeignKey,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
)


metadata_obj = MetaData()

#
# CREATE TABLE airports_data (
#     airport_code character(3) NOT NULL,
#     airport_name jsonb NOT NULL,
#     city jsonb NOT NULL,
#     timezone text NOT NULLForeignKey
# );
airports_data = Table(
    "airports_data",
    metadata_obj,
    Column("airport_code", CHAR(3), primary_key=True),
    Column("airport_name", JSONB, nullable=False),
    Column("city", JSONB, nullable=False),
    Column("timezone", Text, nullable=False),
)


# CREATE TABLE aircrafts_data (
#     aircraft_code character(3) NOT NULL,
#     model jsonb NOT NULL,
#     range integer NOT NULL,
#     CONSTRAINT aircrafts_range_check CHECK ((range > 0))
# );
aircrafts_data = Table(
    "aircrafts_data",
    metadata_obj,
    Column("aircraft_code", CHAR(3), primary_key=True),
    Column("model", JSONB, nullable=False),
    Column(
        "range",
        Integer,
        CheckConstraint("range>0"),
        nullable=False,
    ),
)

#
# CREATE TABLE boarding_passes (
#     ticket_no character(13) NOT NULL,
#     flight_id integer NOT NULL,
#     boarding_no integer NOT NULL,
#     seat_no character varying(4) NOT NULL
# );
boarding_passes = Table(
    "boarding_passes",
    metadata_obj,
    Column("ticket_no", CHAR(13), nullable=False),
    Column("flight_id", Integer, nullable=False, index=True, unique=True),
    Column("boarding_no", Integer, nullable=False),
    Column("seat_no", VARCHAR(4), nullable=False),
    ForeignKeyConstraint(
        ("ticket_no", "flight_id"),
        ("ticket_flights.ticket_no", "ticket_flights.flight_id"),
        name="boarding_passes_ticket_no_fkey",
    ),
    Index(
        "boarding_passes_flight_id_boarding_no_key",
        "flight_id",
        "boarding_no",
        unique=True,
    ),
    Index(
        "boarding_passes_flight_id_seat_no_key",
        "flight_id",
        "seat_no",
        unique=True,
    ),
    Index(
        "boarding_passes_pkey",
        "ticket_no",
        "flight_id",
        unique=True,
    ),
)


# CREATE TABLE bookings (
#     book_ref character(6) NOT NULL,
#     book_date timestamp with time zone NOT NULL,
#     total_amount numeric(10,2) NOT NULL
# );
bookings = Table(
    "bookings",
    metadata_obj,
    Column("book_ref", CHAR(6), primary_key=True),
    Column("book_date", TIMESTAMP(timezone=True), nullable=False),
    Column("total_amount", NUMERIC(10, 2), nullable=False),
)


# CREATE TABLE flights (
#     flight_id integer NOT NULL,
#     flight_no character(6) NOT NULL,
#     scheduled_departure timestamp with time zone NOT NULL,
#     scheduled_arrival timestamp with time zone NOT NULL,
#     departure_airport character(3) NOT NULL,
#     arrival_airport character(3) NOT NULL,
#     status character varying(20) NOT NULL,
#     aircraft_code character(3) NOT NULL,
#     actual_departure timestamp with time zone,
#     actual_arrival timestamp with time zone,
#     CONSTRAINT flights_check CHECK ((scheduled_arrival > scheduled_departure)),
#     CONSTRAINT flights_check1 CHECK (((actual_arrival IS NULL) OR ((actual_departure IS NOT NULL) AND (actual_arrival IS NOT NULL) AND (actual_arrival > actual_departure)))),
#     CONSTRAINT flights_status_check CHECK (((status)::text = ANY (ARRAY[('On Time'::character varying)::text, ('Delayed'::character varying)::text, ('Departed'::character varying)::text, ('Arrived'::character varying)::text, ('Scheduled'::character varying)::text, ('Cancelled'::character varying)::text])))
# );
flights = Table(
    "flights",
    metadata_obj,
    Column("flight_id", Integer, primary_key=True),
    Column("flight_no", CHAR(6), nullable=False),
    Column("scheduled_departure", TIMESTAMP(timezone=True), nullable=False),
    Column("scheduled_arrival", TIMESTAMP(timezone=True), nullable=False),
    Column(
        "departure_airport",
        CHAR(3),
        ForeignKey("airports_data.airport_code"),
        nullable=False,
    ),
    Column(
        "arrival_airport",
        CHAR(3),
        ForeignKey("airports_data.airport_code"),
        nullable=False,
    ),
    Column("status", VARCHAR(20), nullable=False),
    Column(
        "aircraft_code",
        CHAR(3),
        ForeignKey("aircrafts_data.aircraft_code"),
        nullable=False,
    ),
    Column(
        "actual_departure",
        TIMESTAMP(timezone=True),
        nullable=False,
    ),
    Column(
        "actual_arrival",
        TIMESTAMP(timezone=True),
        nullable=False,
    ),
    Index(
        "flights_flight_no_scheduled_departure_key",
        "flight_no",
        "scheduled_departure",
        unique=True,
    ),
    CheckConstraint("scheduled_arrival > scheduled_departure", name="flights_check"),
    CheckConstraint(
        "((actual_arrival IS NULL) OR ((actual_departure IS NOT NULL) AND (actual_arrival IS NOT NULL) AND (actual_arrival > actual_departure)))",
        name="flights_check1",
    ),
    CheckConstraint(
        "((status)::text = ANY (ARRAY[('On Time'::character varying)::text, ('Delayed'::character varying)::text, ('Departed'::character varying)::text, ('Arrived'::character varying)::text, ('Scheduled'::character varying)::text, ('Cancelled'::character varying)::text]))",
        name="flights_status_check",
    ),
)

# CREATE TABLE seats (
#     aircraft_code character(3) NOT NULL,
#     seat_no character varying(4) NOT NULL,
#     fare_conditions character varying(10) NOT NULL,
#     CONSTRAINT seats_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
# );
seats = Table(
    "seats",
    metadata_obj,
    Column(
        "aircraft_code",
        CHAR(3),
        ForeignKey("aircrafts_data.aircraft_code"),
        nullable=False,
    ),
    Column("seat_no", VARCHAR(4), nullable=False),
    Column("fare_conditions", VARCHAR(10), nullable=False),
    PrimaryKeyConstraint("aircraft_code", "seat_no", name="seats_pkey"),
    CheckConstraint(
        "((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text]))",
        name="seats_fare_conditions_check",
    ),
)


# CREATE TABLE ticket_flights (
#     ticket_no character(13) NOT NULL,
#     flight_id integer NOT NULL,
#     fare_conditions character varying(10) NOT NULL,
#     amount numeric(10,2) NOT NULL,
#     CONSTRAINT ticket_flights_amount_check CHECK ((amount >= (0)::numeric)),
#     CONSTRAINT ticket_flights_fare_conditions_check CHECK (((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text])))
# );
ticket_flights = Table(
    "ticket_flights",
    metadata_obj,
    Column("ticket_no", CHAR(13), nullable=False),
    Column("flight_id", Integer, nullable=False),
    Column("fare_conditions", VARCHAR(10), nullable=False),
    Column("amount", NUMERIC(10, 2), nullable=False),
    PrimaryKeyConstraint("ticket_no", "flight_id", name="ticket_flights_pkey"),
    CheckConstraint(
        "(amount >= (0)::numeric)",
        name="ticket_flights_amount_check",
    ),
    CheckConstraint(
        "((fare_conditions)::text = ANY (ARRAY[('Economy'::character varying)::text, ('Comfort'::character varying)::text, ('Business'::character varying)::text]))",
        name="ticket_flights_fare_conditions_check",
    ),
)


# CREATE TABLE tickets (
#     ticket_no character(13) NOT NULL,
#     book_ref character(6) NOT NULL,
#     passenger_id character varying(20) NOT NULL,
#     passenger_name text NOT NULL,
#     contact_data jsonb
# );
tickets = Table(
    "tickets",
    metadata_obj,
    Column("ticket_no", CHAR(13), primary_key=True),
    Column("book_ref", CHAR(6), ForeignKey("bookings.book_ref"), nullable=False),
    Column("passenger_id", VARCHAR(20), nullable=False),
    Column("contact_data", JSONB, nullable=False),
)


async def async_main():
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)

    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.drop_all)
        await conn.run_sync(metadata_obj.create_all)

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(async_main())

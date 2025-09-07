from sqlalchemy import Table, Column, Integer, String
from app.db import metadata, engine

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
)

# Create tables in the database
metadata.create_all(engine)

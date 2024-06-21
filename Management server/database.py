import sqlalchemy
import databases

# Define the database URL
DATABASE_URL = "mysql+aiomysql://username:password@127.0.0.1/dbname"

# Create the database object
database = databases.Database(DATABASE_URL)

# Create the metadata object
metadata = sqlalchemy.MetaData()

# Define the submissions table
submissions = sqlalchemy.Table(
    "submissions",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("code", sqlalchemy.Text),
    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)

# Create the engine and create all tables
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

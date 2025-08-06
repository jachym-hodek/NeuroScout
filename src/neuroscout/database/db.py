from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///otevrenaveda.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define the Internships model
class Internships(Base):
    __tablename__ = "internships"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=True)
    field = Column(String, nullable=True)
    title = Column(String, nullable=True)
    mentor = Column(String, nullable=True)
    institution = Column(String, nullable=True)
    application_deadline = Column(String, nullable=True)
    start_date = Column(String, nullable=True)
    eligibility = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    hours_per_month = Column(String, nullable=True)
    time_details = Column(String, nullable=True)
    location = Column(String, nullable=True)
    description = Column(String, nullable=True)
    link = Column(String, nullable=True)


class Competitions(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    application_deadline = Column(String, nullable=True)
    start_date = Column(String, nullable=True)
    eligibility = Column(String, nullable=True)
    end_date = Column(String, nullable=True)
    prizes = Column(String, nullable=True)
    link = Column(String, nullable=True)

# Initialize the database and create tables
def init_db():
    Base.metadata.create_all(bind=engine)
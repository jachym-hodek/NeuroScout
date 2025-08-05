from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///otevrenaveda.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class OtevrenaVedaOpportunity(Base):
    __tablename__ = "otevrenaveda_opportunities"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    field = Column(String)
    title = Column(String)
    mentor = Column(String)
    institution = Column(String)
    duration = Column(String)
    hours_per_month = Column(String)
    time_details = Column(String)
    location = Column(String)
    description = Column(String)
    student = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
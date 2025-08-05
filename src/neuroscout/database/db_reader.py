from db import SessionLocal, OtevrenaVedaOpportunity

def get_all_opportunities():
    session = SessionLocal()
    try:
        opportunities = session.query(OtevrenaVedaOpportunity).all()
        return opportunities
    finally:
        session.close()

if __name__ == "__main__":
    for opp in get_all_opportunities():
        print(f"{opp.id}: {opp.title}: {opp.city}, {opp.field}")
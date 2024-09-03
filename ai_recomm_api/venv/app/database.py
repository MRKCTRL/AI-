from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlaclemy.orm import sessionmaker
from sqlalchemy.orm import selectinLoad
from sqlalchemy import text



SQLALCHEMY_DATABASE_URL="postgresql://user:password@localhost/dbname"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommitt=False, autoflush=False,bind=engine)
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_user_with_interactions(db:Session,user_id:int):
    return db.query(models.User).options(selectinLoad(models.User.interactions))


def search_content(db:Session, query:str):
    return db.execute(text("SELECT * FROM content WHERE to_tsvector('english', title|| ' ' || description) @@ to_tsquery(:query)"), 'query':query}).fetchall()
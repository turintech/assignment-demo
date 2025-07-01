from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Word(Base):
    __tablename__ = "words"
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True, nullable=False)


class WordCreate(BaseModel):
    word: str


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.put("/word")
def put_word(word: WordCreate, db: Session = Depends(get_db)):
    db_word = db.query(Word).filter(Word.word == word.word).first()
    if db_word:
        raise HTTPException(status_code=400, detail="Word already exists")
    new_word = Word(word=word.word)
    db.add(new_word)
    db.commit()
    db.refresh(new_word)
    return {"id": new_word.id, "word": new_word.word}


@app.get("/words")
def get_words(db: Session = Depends(get_db)):
    words = db.query(Word).all()
    return [{"id": w.id, "word": w.word} for w in words]

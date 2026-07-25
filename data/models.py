from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base


'''
class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    size = Column(String)
    speed = Column(Integer)
    description = Column(String)
    features = Column(String)

class SubSpecies(Base):
    __tablename__ = "subspecies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"))
    description = Column(String)
    features = Column(String)

class Background(Base):
    __tablename__ = "backgrounds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)
    features = Column(String)

class Spell(Base):
    __tablename__ = "spells"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    level = Column(Integer, nullable=False)
    description = Column(String)
    spell_type = Column(String)

class ClassSpells(Base):
    __tablename__ = "class_spells"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    spell_id = Column(Integer, ForeignKey("spells.id"))
    '''
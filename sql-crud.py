from inspect import trace
from tkinter import S
from django import db
from matplotlib import artist
from more_itertools import first, last
from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Executing the instructions form the "chinook" database
db = create_engine('postgresql:///chinook')
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new session of a sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

aleksei_konovalov = Programmer(
    first_name="Aleksei",
    last_name="Konovalov",
    gender="M",
    nationality="Russian",
    famous_for="Some cool stuff"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(aleksei_konovalov)


# commit or session to the database
# session.commit()

# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Another cool stuff"

# session.commit()

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     else:
#         person.gender = "Male"
#     session.commit()

# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# if programmer is not None:
#     print("Programmer found:", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )

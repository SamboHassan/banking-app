from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "Customer"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    email_address = db.Column(db.String(255), nullable=False)
    comfirmed = db.Column(db.Boolean, default=False)


class Account(db.Model):
    __tablename__ = "Account"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("Customer.id"))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    balance = db.Column(db.Numeric(19, 2))


# class Transaction(db.Model):
#     __tablename__ = "Transaction"

#     id = db.Column(db.Integer, primary_key=True)
#     source_id = db.Column(db.Integer(), db.ForeignKey("Customer.id"))
#     target_id = db.Column(db.Integer(), db.ForeignKey("Customer.id"))
#     amount = db.Column(db.Numeric(19, 2))
#     balance = db.Column(db.Numeric(19, 2))
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

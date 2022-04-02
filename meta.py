from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

from engine import engine

meta = MetaData()
# meta = MetaData(bind=engine)
# MetaData.reflect(meta)

users = Table('users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', meta,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

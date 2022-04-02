from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://ghostown:ghostown@localhost:5455/ghostown", echo=True, future=True)

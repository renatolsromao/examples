import os

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = sqlalchemy.create_engine(os.getenv('POSTGRES_ENGINE'), use_batch_mode=True)

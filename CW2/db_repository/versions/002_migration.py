from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
association = Table('association', post_meta,
    Column('url_id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer, primary_key=True, nullable=False),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_name', String(length=64)),
    Column('email', String(length=500)),
    Column('password', String(length=500)),
    Column('first_name', String(length=500)),
    Column('last_name', String(length=500)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['association'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['association'].drop()
    post_meta.tables['user'].drop()

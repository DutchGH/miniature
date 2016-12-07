from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
association = Table('association', pre_meta,
    Column('url_id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER, primary_key=True, nullable=False),
)

usergen = Table('usergen', post_meta,
    Column('user_id', Integer),
    Column('url_table_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].drop()
    post_meta.tables['usergen'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['association'].create()
    post_meta.tables['usergen'].drop()

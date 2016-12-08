from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
gens = Table('gens', pre_meta,
    Column('url_id', INTEGER),
    Column('user_id', INTEGER),
)

gens = Table('gens', post_meta,
    Column('generator_id', Integer),
    Column('url_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['gens'].columns['user_id'].drop()
    post_meta.tables['gens'].columns['generator_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['gens'].columns['user_id'].create()
    post_meta.tables['gens'].columns['generator_id'].drop()

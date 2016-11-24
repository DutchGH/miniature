from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
url = Table('url', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=100)),
    Column('long_url', TEXT),
)

url = Table('url', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('url', String(length=100)),
    Column('long_url', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['url'].columns['name'].drop()
    post_meta.tables['url'].columns['url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['url'].columns['name'].create()
    post_meta.tables['url'].columns['url'].drop()

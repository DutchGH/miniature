from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
priority = Table('priority', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('value', INTEGER),
)

todo = Table('todo', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('priority_id', INTEGER),
    Column('description', VARCHAR),
    Column('creation_date', DATE),
    Column('is_done', BOOLEAN),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['priority'].drop()
    pre_meta.tables['todo'].columns['priority_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['priority'].create()
    pre_meta.tables['todo'].columns['priority_id'].create()

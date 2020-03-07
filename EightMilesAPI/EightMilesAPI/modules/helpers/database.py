from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import SESSION_OPTS

engine = create_engine(SESSION_OPTS['session.url'], pool_size=40, max_overflow=1, pool_recycle=3600, echo=True)
db_session = scoped_session(sessionmaker(autocommit=True,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from modules.model.usersmodel import UserStatus, UserType
    import modules.model.usersmodel

    Base.metadata.drop_all(bind=engine)
    # add_status = [UserStatus(0, 'inactive'),UserStatus(1, 'active')]
    # add_type = [UserType(0, 'unregister'),UserType(1, 'admin'),UserType(2, 'provider')]    
    Base.metadata.create_all(bind=engine)

    #db_session.add_all([
    #    UserStatus(status=0, desc='inactive'), 
    #    UserStatus(status=1, desc='active')
    #    ])
    #db_session.add_all([
    #    UserType(usrtype=0, desc='unregister'), 
    #    UserType(usrtype=1, desc='admin'), 
    #    UserType(usrtype=2, desc='provider')
    #    ])
    db_session.commit()



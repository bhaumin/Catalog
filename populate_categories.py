from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category

engine = create_engine('sqlite:///catalog.db')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Category - Soccer
soccer = Category(name="Soccer")

session.add(soccer)
session.commit()

# Category - Basketball
basketball = Category(name="Basketball")

session.add(basketball)
session.commit()

# Category - Baseball
baseball = Category(name="Baseball")

session.add(baseball)
session.commit()

# Category - Frisbee
frisbee = Category(name="Frisbee")

session.add(frisbee)
session.commit()

# Category - Snowboarding
snowboarding = Category(name="Snowboarding")

session.add(snowboarding)
session.commit()

# Category - Rock Climbing
rockclimbing = Category(name="Rock Climbing")

session.add(rockclimbing)
session.commit()

# Category - Foosball
foosball = Category(name="Foosball")

session.add(foosball)
session.commit()

# Category - Skating
skating = Category(name="Skating")

session.add(skating)
session.commit()

# Category - Hockey
hockey = Category(name="Hockey")

session.add(hockey)
session.commit()


print "added categories!"

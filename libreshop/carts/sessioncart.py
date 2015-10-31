import logging

logger = logging.getLogger(__name__)

UUID = 'b37d96da-006e-4ba1-945c-ca4f3b318eea'

class SessionCart(list):

    def __init__(self, session):

        logger.info('Getting %s...' % self.__class__.__name__)

        if not session.has_key(UUID):
            logger.info('Could not find a %s!' % self.__class__.__name__)
            session[UUID] = self
        else:
            logger.info('Found %s!' % self.__class__.__name__)
            self += session.get(UUID)

        self.session = session


    def add(self, product_id):
        logger.debug('request.session: %s' % self.session[UUID])
        logger.info('Adding product to %s...' % self.__class__.__name__)

        self.append(product_id)
        self.session.modified = True

        logger.info('Added product to %s.' % self.__class__.__name__)
        logger.debug('request.session: %s' % self.session[UUID])


    @property
    def count(self):
        return len(self)


    @property
    def has_products(self):
        return bool(len(self))
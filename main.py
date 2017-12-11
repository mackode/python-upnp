#!/usr/bin/env python3

import upnpthread
import logging

logger = logging.getLogger("golem.task.main")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-23s %(levelname)-6s %(threadName)-12s %(message)s')

logger.debug("MAIN")
if __name__ == '__main__':
    upnp = upnpthread.UpnpThread([3282, 40102, 40103])
    upnp.start()
    upnp.join()

    upnp = upnpthread.UpnpThread([3282, 40102, 40103], True)
    upnp.start()
    upnp.join()

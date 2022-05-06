import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/flaskapp')
from flaskapp import app as application

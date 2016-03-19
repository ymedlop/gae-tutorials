# https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring

"""`appengine_config` gets loaded when starting a new application instance."""
from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
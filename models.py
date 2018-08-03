'''datastores for posts, music, resources, etc'''

from google.appengine.ext import ndb

# Ezan!! Add your login/user datastore in here when you are done

class Post(ndb.Model):
    #change the user id requirement to true later when incorporating Ezan's code
    post_user_id = ndb.StringProperty(required=False)
    post_content = ndb.StringProperty(required=True)
    post_time = ndb.DateTimeProperty(auto_now_add=True)

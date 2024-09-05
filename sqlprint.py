from flaskblog import app, db
from flaskblog.models import User

# Push application context
with app.app_context():
    # Query the first user
    user = User.query.first()
    print(user)

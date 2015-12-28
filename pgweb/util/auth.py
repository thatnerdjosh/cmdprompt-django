from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db import connection

from pgweb.core.models import UserProfile

# Special version of the authentication backend, so we can deal with migration
# of accounts from the old community login system. Once we consider all accounts
# migrated, we can remove this one and use the default backend.
class AuthBackend(ModelBackend):
	def authenticate(self, username=None, password=None):
		user = User.objects.get(username=username.lower())

		# If user is found, check the password using the django
		# methods alone.
		if user.check_password(password):
			return user

		# User found but password wrong --> tell django it is wrong
		return None

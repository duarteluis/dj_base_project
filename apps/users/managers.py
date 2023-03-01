from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email must be provided")

        user = self.model(email=self.normalize_email(email))
        user.type = user.TYPEPROFILE.USER
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.type = user.TYPEPROFILE.ADMIN
        user.save(using=self._db)
        return user

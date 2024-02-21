from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, password, **kwargs):
        if 'email' not in kwargs:
            raise ValueError('Users must have email address')

        user = self.model(
            email=kwargs['email']
        )
        user.set_password(password)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

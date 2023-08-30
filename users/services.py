from random import randint

from django.conf import settings
from users.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy

from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail


def add_group(user):
    group = Group.objects.get(name='Service_user')
    user.groups.add(group)
    user.save()


def send_registration_mail(user):
    user.is_active = False
    user.save()
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
    current_site = settings.SITE_NAME
    send_mail(
        subject='Регистрация на сайте',
        message=f'Вы зарегистрировались на нашей платформе, пожалуйста подтвердите свой email: '
                f'http://{current_site}{activation_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )


def send_reset_password_mail(email):
    user = User.objects.get(email=email)
    new_password = "".join([str(randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Смена пароля',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    user.set_password(new_password)
    user.save()

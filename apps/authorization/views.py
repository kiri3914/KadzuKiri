from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from rest_framework.views import APIView
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializers




# Список пользователей и редактирование данных пользователя
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def create(self , request , *args , **kwargs):
        # регистрации пользователя
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Создание токена и ссылки для подтверждения
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        confirmation_link = self.request.build_absolute_uri(
            reverse('confirm-email' , kwargs={'uidb64': uid, 'token': token})
        )

        # Отправка письма с ссылкой для подтверждения
        email_subject = 'Подтверждение регистрации'
        email_message = render_to_string('registration_confirmation_email.html', {
            'user': user ,
            'confirmation_link': confirmation_link ,
        })
        print(email_message)
        send_mail(email_subject , email_message , settings.DEFAULT_FROM_EMAIL ,
                  [user.email] , html_message=email_message)

        return Response({'detail': 'Подтверждения  Email отправлена на почту!'})


# Подтверждение Email адреса
class ConfirmEmailView(APIView):
    def get(self , request , uidb64 , token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError , ValueError , OverflowError):
            return Response({'detail': 'Недействительная ссылка для подтверждения.'} , status=HTTP_400_BAD_REQUEST)

        if user and default_token_generator.check_token(user , token):
            user.email_confirmed = True
            user.is_active = True
            user.save()
            return Response({'detail': 'Email успешно подтвержден!'})
        else:
            return Response({'detail': 'Недействительный токен подтверждения.'})
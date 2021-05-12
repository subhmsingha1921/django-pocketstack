# from django.conf import settings
# from django.shortcuts import redirect
# from django.http import HttpResponsePermanentRedirect, HttpResponse

# from allauth.account.adapter import DefaultAccountAdapter


# # class CustomRedirect(HttpResponsePermanentRedirect):
# #     allowed_schemes = ['exp', 'http', 'https']


# # class MyAccountAdapter(DefaultAccountAdapter):

# #     def get_email_confirmation_redirect_url(self, request):
# #         # return CustomRedirect('exp://127.0.0.1:19000/--/auth/login')
# #         response = HttpResponse("", status=302)
# #         response['Location'] = "exp://127.0.0.1:19000/--/auth/login"
# #         return response


# class MyAccountAdapter(DefaultAccountAdapter):

#     def send_mail(self, template_prefix, email, context):
#         context['activate_url'] = settings.EXPO_LOGIN_URL + 'auth/registration/account-confirm-email/' + context['key']
#         msg = self.render_mail(template_prefix, email, context)
#         msg.send()
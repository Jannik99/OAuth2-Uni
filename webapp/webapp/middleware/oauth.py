from authlib.integrations.django_client import OAuth
from django.conf import settings


class OAuthMiddleware:
    def __init__(self):
        self.oauth = OAuth()
        self.oauth.register(
            name=settings.OAUTH_CLIENT_NAME,
            client_id=settings.OAUTH_CLIENT['client_id'],
            client_secret=settings.OAUTH_CLIENT['client_secret'],
            access_token_url=settings.OAUTH_CLIENT['access_token_url'],
            authorize_url=settings.OAUTH_CLIENT['authorize_url'],
            api_base_url='https://api.github.com/',
            client_kwargs={'scope': 'user:email'},
        )
        github = self.oauth.github

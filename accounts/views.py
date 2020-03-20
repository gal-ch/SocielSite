
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import \
    login as django_login, \
    logout as django_logout, \
    get_user_model
User = get_user_model()


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super(SocialAccountAdapter, self).save_user(request, sociallogin, form)
        social_app_name = sociallogin.account.provider.upper()
        extra_data = sociallogin.account.extra_data
        if social_app_name == "FACEBOOK":
            profile_url = "https://graph.facebook.com/v2.4/{user_id}/picture?type=square&height={height}&width={width}&return_ssl_rources=1".format(
                user_id=extra_data['id'],
                height=150,
                width=150,
            )
            User.objects.get_or_create_facebook_user(user_pk=user.pk, extra_data=extra_data, profile_url=profile_url)

        return user





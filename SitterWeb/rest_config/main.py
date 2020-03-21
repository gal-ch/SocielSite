import datetime


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
        'type': 'basic'
        }
    },
    'DOC_EXPANSION': 'None',
    'JSON_EDITOR': True
}

JWT_AUTH = {
         'JWT_RESPONSE_PAYLOAD_HANDLER':
         'accounts.utils.jwt_response_payload_handler',
         'JWT_ALLOW_REFRESH': True,
         'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=600),
         }
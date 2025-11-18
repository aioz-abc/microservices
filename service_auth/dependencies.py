from .service_impl import AuthService

auth_service = AuthService()


def get_auth_service():
    return auth_service

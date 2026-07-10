from services.auth_service import AuthService
from models.owner import Owner

from exceptions import *

class AuthController:
    def __init__(self,authService:AuthService):
        self.service = authService


    def login(self,email,password):
        try:
            return self.service.login(email,password)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")
        except AuthorizationError as e:
            print(f"Authorization Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def register(self,owner:Owner):
        try:
            return self.service.register(owner)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")
        except AuthorizationError as e:
            print(f"Authorization Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def logout(self):
        try:
            self.service.logout()
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")
        except AuthorizationError as e:
            print(f"Authorization Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def current_user(self):
        try:
            return self.service.get_current_user()
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")
        except AuthorizationError as e:
            print(f"Authorization Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def change_password(self,oldPassword:str,newPassword:str):
        try:
            self.service.change_password(oldPassword,newPassword)
        except ValidationError as e:
            print(f"Validation Error: {e}")
        except AuthenticationError as e:
            print(f"Authentication Error: {e}")
        except AuthorizationError as e:
            print(f"Authorization Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


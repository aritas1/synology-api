from typing import Optional, Any
from . import auth


class BaseApi(object):
    def __init__(self,
                 ip_address: Optional[str] = "",
                 port: Optional[str] = "",
                 username: Optional[str] = "",
                 password: Optional[str] = "",
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None,
                 application: str = "Core",
                 session: Optional[auth.Authentication] = None
                 ) -> None:

        if session is None:
            self.session: auth.Authentication = auth.Authentication(ip_address, port, username, password,
                                                                    secure, cert_verify, dsm_version, debug,
                                                                    otp_code, application)

            # login only on if no session is provided,
            # caller don't care about session manage, we need to set up things
            self.session.login()
            self.session.get_api_list()
        else:
            self.session = session

        self._application = application
        self.request_data: Any = self.session.request_data

        # all core modules use the self.core_list variable
        if self._application == "Core":
            self.core_list: Any = self.session.app_api_list

        self.gen_list: Any = self.session.full_api_list
        self._sid: str = self.session.sid
        self.base_url: str = self.session.base_url

    def logout(self) -> None:
        self.session.logout(self._application)

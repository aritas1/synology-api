from __future__ import annotations
from typing import Optional
from . import base_api_core


class ActiveBackupGSuite(base_api_core.Core):
    def __init__(self,
                 ip_address: str,
                 port: str,
                 username: str,
                 password: str,
                 secure: bool = False,
                 cert_verify: bool = False,
                 dsm_version: int = 7,
                 debug: bool = True,
                 otp_code: Optional[str] = None
                 ) -> None:
        super(ActiveBackupGSuite, self).__init__(ip_address, port, username, password, secure, cert_verify,
                                                 dsm_version, debug, otp_code)
        return

    def activation_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupGSuite'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_activation'}

        return self.request_data(api_name, api_path, req_param)

    def list_tasks(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupGSuite'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_tasks'}

        return self.request_data(api_name, api_path, req_param)

    def get_general_log(self, offset: int = 0, limit: int = 200) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupGSuite'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_general_log',
                     'offset': offset,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

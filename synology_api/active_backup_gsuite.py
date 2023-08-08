from __future__ import annotations

from enum import Enum

from . import base_api


class ActiveBackupGSuiteStatus(Enum):
    # as seen in the wild
    SUCCESS = 1,
    BACKUP_IN_PROGRESS = 3,  # ??
    SUCCESS_NO_DATA_TRANSFERRED = 4,  # ??


class ActiveBackupGSuiteTaskStatus(Enum):
    # the is also a task status that may differ from status?
    pass


class ActiveBackupGSuite(base_api.BaseApi):

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

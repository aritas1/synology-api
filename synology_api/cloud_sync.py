from __future__ import annotations

from enum import Enum
from . import base_api


class CloudSyncLogLevel(Enum):
    ALL = -1
    INFO = 0
    WARNING = 1
    ERROR = 2


class CloudSyncAction(Enum):
    ALL = -1
    DOWNLOAD = 1
    UPLOAD = 2
    DELETE_LOCAL = 3
    DELETE_REMOTE = 0
    RENAME_REMOTE = 4
    MERGE = 8
    DELETE_MERGE = 9


# Note: error/warning status codes missing
class CloudSyncLinkStatus(Enum):
    OK = 1


# also used for the TryStatus
# Note: error/warning status codes missing
class CloudSyncStatus(Enum):
    OK = "uptodate"


class CloudSyncGroupingTypes(Enum):
    by_cloud = "group_by_cloud_type"
    by_user = "group_by_user"


class CloudSync(base_api.BaseApi):

    def list_conn(self, group_by: CloudSyncGroupingTypes = CloudSyncGroupingTypes.by_user) -> dict[str, object] | str:
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_conn',
                     'is_tray': False,
                     'group_by': group_by}

        return self.request_data(api_name, api_path, req_param)

    def get_property(self, connection_id:  int) -> dict[str, object] | str:
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_property',
                     'connection_id': connection_id}

        return self.request_data(api_name, api_path, req_param)

    def list_sess(self, connection_id:  int) -> dict[str, object] | str:
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_sess',
                     'connection_id': connection_id}

        return self.request_data(api_name, api_path, req_param)

    def get_log(self,
                connection_id:  int,
                offset: int = 0,
                limit: int = 200,
                log_level: CloudSyncLogLevel = CloudSyncLogLevel.ALL,
                action: CloudSyncAction = CloudSyncLogLevel.ALL,
                keyword: str = "",
                date_from: int = 0,
                date_to: int = 0
                ) -> dict[str, object] | str:
        api_name = 'SYNO.CloudSync'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_log',
                     'connection_id': connection_id,
                     'offset': offset,
                     'limit': limit,
                     'log_level': log_level,
                     'action': action,
                     'keyword': keyword,
                     'date_from': date_from,
                     'date_to': date_to}

        return self.request_data(api_name, api_path, req_param)

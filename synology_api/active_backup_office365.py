from __future__ import annotations

from enum import Enum
from . import base_api

# error codes reverse engineered on 2.5.2-12818 from the description of the get_general_log and get_all_log endpoint
office365_error_codes: dict[int, str] = {
    # Note: log_type is not consistent for every error code. sometimes an error is considered ok and sometimes not.
    # log_type = success
    0: "Success. Nothing. Data unchanged?",
    -3: 'System error.',  # strange, type is success ..

    # 8X? codes also fire if nothing was backed up or nothing changed.
    -84: 'Success. OneDrive.',
    # No OneDrive data available. Make sure that OneDrive for Business is enabled and that users are logged in.
    -85: 'Success. Exchange Mail/Mail-Archive.',
    # No Mail/Mail-Archive data are available for backup since the mail service has not been enabled or logged in.
    -86: 'Success. Exchange Contacts.',
    -87: 'Success. Exchange Calendar.',

    -95: 'No archive mailbox data are available for backup since the archive mailbox service has not been enabled or logged in.',
    -97: 'No OneDrive data available for backup. Make sure that OneDrive for Business is enabled and that users are logged in.',

    # log_type = failed
    -11: 'Unable to verify the SSL certificate.',
    -13: 'Server error.',
    -26: 'Cannot resolve the IP address of the server.',
    -28: 'Server has no response.',  # the description sometimes contains server response details
    -80: 'The system is busy because too many API requests are being submitted now. Please try again later.',
    -109: 'The user may have been renamed or deleted. Please check your user list of Microsoft 365 and try again later.',
    -114: 'The Microsoft server returned an authentication error. Please check if your mailbox exists in Exchange Online (not on-premises) and check if it is accessible.',
    -156: 'The Microsoft server is busy. Please try again later.',
    -157: 'An error occurred in the Microsoft server. Please try again later.',
    -220: 'No contact data were backed up. The tenant does not have a SharePoint license.',
    -303: 'The site has been deleted.',  # Sharepoint?
    -608: 'The Microsoft server returned an error in the operation on Exchange Online mailboxes. Please contact Microsoft support. ',
    -1000: 'An unknown error occurred. Please try again later.',

    # log_type = warning
    -1: 'Task aborted.',
    -2: 'Detected a network connection failure. Please check if your firewall settings are correct.',
    -14: 'The operation timed out.',
    -32: 'File is not supported.',
    -63: 'Server file cannot be found.',
    -70: 'The file on the server is corrupt.',
    -118: 'No service (mail, calendar) data were backed up.',
    -162: 'The file was skipped due to a temporary issue on the Microsoft server.',
    -400: 'Backup of shared calendars is not supported.',
}


class ActiveBackupOffice365ServiceTypes(Enum):
    # User
    DRIVE = 0
    MAIL = 1
    CONTACT = 2
    CALENDAR = 3
    ARCHIVE_MAIL = 4
    SITE = 5  # sharepoint
    GROUP_MAIL = 6
    GROUP_CALENDAR = 7  # educated guess
    MYSITE = 8  # sharepoint personal
    TEAMS = 9  # educated guess


class ActiveBackupOffice365LogTypes(Enum):
    ALL = None
    INFO = 0
    ERROR = 1
    WARNING = 2


class ActiveBackupOffice365LogCategory(Enum):
    ALL = None
    BACKUP = 0
    DELEGATION = 2
    VERIFICATION = 3
    GENERAL = 4


class ActiveBackupOffice365Status(Enum):
    ALL = None
    # global task status
    SUCCESS = 1
    PARTIAL_FAILED = 2
    #FAILED = 3????


class ActiveBackupOffice365TaskStatus(Enum):
    ALL = None
    #TASK_SUCCESS = 4?????
    TASK_FAILED = 5
    TASK_PARTIAL_FAILED = 6


class ActiveBackupOffice365(base_api.BaseApi):

    def activation_status(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_activation'}

        return self.request_data(api_name, api_path, req_param)

    def get_worker_count(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_worker_count'}

        return self.request_data(api_name, api_path, req_param)

    def list_local_user(self,
                        task_id: int,
                        offset: int = 0,
                        limit: int = 200
                        ) -> dict[str, object] | str:
        """
        returns a mix of "user_list", "team_list", "my_site_list" and "general_site_list"
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_local_user',
                     'task_id': task_id,
                     'offset': offset,
                     'limit': limit,
                     #'is_remove_storage': True,
                     }

        return self.request_data(api_name, api_path, req_param)

    def list_local_group(self,
                        task_id: int,
                        offset: int = 0,
                        limit: int = 200
                        ) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_local_group',
                     'task_id': task_id,
                     'offset': offset,
                     'limit': limit,
                     'group_type': 0  # all = 0, security = 1, distribution_list = 2, email security = 3
                     }

        return self.request_data(api_name, api_path, req_param)


    def list_tasks(self) -> dict[str, object] | str:
        """
        returns a mix of "tasks", "event_log", "service_usage" and "users"
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_tasks'}

        return self.request_data(api_name, api_path, req_param)

    def get_task_log(self, task_id: int, task_execution_id: int) -> dict[str, object] | str:
        """
        returns the logs for a specific execution of a task
        NOTE: results may be identical to get_task_all_log
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_task_log',
                     'task_id': task_id,
                     'task_execution_id': task_execution_id}

        return self.request_data(api_name, api_path, req_param)

    def get_task_combined_log(self,
                              task_id: int,
                              task_execution_id: int,
                              offset: int = 0,
                              limit: int = 200) -> dict[str, object] | str:
        """
        returns a list of combined logs per o365 user/entity with detailed status codes for the individual o365 service
        but not alle individual log entries
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'list_local_all_service',
                     'task_id': task_id,
                     'task_execution_id': task_execution_id,
                     'offset': offset,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def get_task_all_log(self,
                         task_id: int,
                         task_execution_id: int,
                         offset: int = 0,
                         limit: int = 200) -> dict[str, object] | str:
        """
        return all log entry for the task execution
        NOTE: results may be identical to get_task_execution_log
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_all_log',
                     'task_id': task_id,
                     'task_execution_id': task_execution_id,
                     'offset': offset,
                     'limit': limit}

        return self.request_data(api_name, api_path, req_param)

    def get_general_log(self,
                       offset: int = 0,
                       limit: int = 200,
                       log_type: int = ActiveBackupOffice365LogTypes.ALL) -> dict[str, object] | str:
        """
        returns short logs for all tasks
        """
        api_name = 'SYNO.ActiveBackupOffice365'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': info['minVersion'],
                     'method': 'get_general_log',
                     'offset': offset,
                     'limit': limit}

        if log_type is not None:
            req_param['log_type'] = log_type

        return self.request_data(api_name, api_path, req_param)

from __future__ import annotations
from . import base_api

import time


class ActiveBackupBusiness(base_api.BaseApi):

    def list_vm_hypervisor(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Inventory'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list'}

        return self.request_data(api_name, api_path, req_param)

    def list_device_transfer_size(self) -> dict[str, object] | str:
        api_name = 'SYNO.ActiveBackup.Overview'
        info = self.gen_list[api_name]
        api_path = info['path']

        req_param = {'version': '1',
                     'method': 'list_device_transfer_size',
                     'time_start': int(time.time() - 86400),
                     'time_end': int(time.time())}

        return self.request_data(api_name, api_path, req_param)

import glob
import os
import sys
import configparser

from genicam2.genapi import NodeMap
from genicam2.gentl import DeviceInfoList, DeviceInfo, Device
from harvesters.core import Harvester
from PyQt5 import QtCore

import arch


class Camera(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.harvester = Harvester()
        self.acquirer = None

    def load_cti_from_env(self):
        if arch.is_64bits:
            env_name = "GENICAM_GENTL64_PATH"
        else:
            env_name = "GENICAM_GENTL32_PATH"

        genicam_paths = os.environ[env_name].split(os.pathsep)
        cti_files = glob.glob(os.path.join(genicam_paths, "*.cti"))

        for cti in cti_files:
            self.harvester.add_cti_file(cti)

    def reload_device(self):
        self.harvester.update_device_info_list()

    def list_devices(self, reload=False) -> DeviceInfoList:
        if reload:
            self.reload_device()
        return self.harvester.device_info_list

    def use_device(self, cam_id, cfg_file):
        devices = self.list_devices()

        self.acquirer = self.harvester.create_image_acquirer(id_=cam_id)

        parser = configparser.ConfigParser()
        parser.read(cfg_file)
        config: dict = parser["DEVICE_CONFIG"]
        for k, v in config.items():
            node_map: NodeMap = self.acquirer.device.node_map


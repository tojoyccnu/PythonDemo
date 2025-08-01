#!/usr/bin/env python3

from service.basic_discovery import BasicDiscoverer

class Discoverer(BasicDiscoverer):
    def discovery(self, confpath):
        data = ['s3_1', 's3_2']
        return data

    def get_instances(self, confpath):
        "Runs discovery method and packs result into JSON"
        return 's3'
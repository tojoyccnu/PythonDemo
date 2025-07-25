#!/usr/bin/env python3
from service import s3
from service import ec2
from service.basic_discovery import BasicDiscoverer

class Discoverer(BasicDiscoverer):
    def __init__(self):
        self.s3 = s3.Discoverer()
        self.ec2 = ec2.Discoverer()

    def discovery(self, confpath):
        data = self.s3.discovery(confpath) + self.ec2.discovery(confpath)
        return data

    def get_instances(self, confpath):
        "Runs discovery method and packs result into JSON"
        return self.s3.get_instances(confpath) + self.ec2.get_instances(confpath)
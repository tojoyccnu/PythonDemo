#!/usr/bin/env python3

class BasicDiscoverer(object):
    def get_instances(self, confpath):
        "Runs discovery method and packs result into JSON"
        raise NotImplementedError

    def discovery(self, confpath):
        "Method that should be overriden inside inherited classes"
        raise NotImplementedError

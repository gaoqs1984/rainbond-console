# -*- coding: utf8 -*-


class ErrBackupNotFound(Exception):
    def __init__(self, sid):
        msg = "error not found backup for service(service_id={})".format(sid)
        super(ErrBackupNotFound, self).__init__(msg)


class ErrVersionAlreadyExists(Exception):
    def __init__(self):
        msg = "version already exists"
        super(ErrVersionAlreadyExists, self).__init__(msg)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import struct
import time
import threading
from collections import OrderedDict

from pocsuite3.lib.core.common import get_host_ip
from pocsuite3.api import OptString
from pocsuite3.lib.utils import random_str
from pocsuite3.api import (
    Output, POCBase, register_poc, requests, logger,
    get_listener_ip, get_listener_port
)


class LearnPOC(POCBase):
    vulID = ''
    version = '1.0'
    author = ['']
    vulDate = ''
    createDate = ''
    updateDate = ''
    references = ['']
    name = 'Learning PocSuite3 (cve-2022-none)'
    appPowerLink = 'https://www.bing.com'
    appName = 'bing'
    appVersion = 'Multi'
    vulType = 'rce'
    desc = ''
    samples = ['']
    install_requires = []
    url = 'http://www.bing.com'

    def _check(self):
        self.url = self.url.rstrip('/')
        res = requests.get(self.url)
        return True

    def _rce(self, cmd='id', echo=True):
        result = {
                'msg': 'rce got!',
                'flag': 'abcd',
                'VerifyInfo': {}
                }
        return result

    # pocsuite -u http://www.github.com -r poc.py --verify
    def _verify(self):
        result = {}
        result['VerifyInfo'] = {}
        result['VerifyInfo']['URL'] = self.url
        result['VerifyInfo']['cmd'] = 'OK'
        return self.parse_output(result)

    def _options(self):
        o = OrderedDict()
        o['cmd'] = OptString('ps', description='The command to execute')
        return o

    # pocsuite -r poc.py -u www.github.com --attack --ppt
    def _attack(self):
        result = {}
        result['VerifyInfo'] = {}
        result['VerifyInfo']['URL'] = self.url
        result['VerifyInfo']['cmd'] = 'ls'
        return self.parse_output(result)

    # pocsuite -r poc.py -u www.github.com --shell --ppt
    def _shell(self):
        if not self._check():
            return

        cmd = (
            f'date'
        )
        try:
            self._rce(cmd, echo=False)
        except Exception:
            pass
        time.sleep(5)

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output


register_poc(LearnPOC)
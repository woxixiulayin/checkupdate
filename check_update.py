#!coding: utf-8

import logging
import subprocess
import os
from sendmail import send_mail
#
# Setup logging format
#
FORMAT = "%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s"
DATEFMT = "%H:%M:%S"
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)

_logger = logging.getLogger()

logger =_logger

def shellCmd(cmd):
    _logger.debug('[running] %s' %
                  ' '.join(["" if x == None else x for x in cmd]))
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError, e:
        _logger.debug('CalledProcessError: %s' % str(e))
        return (e.returncode, e.output)
    except Exception, e:
        _logger.error('exception: %s' % str(e))
        return (1, str(e))
    for m in out.split('\n'):
        _logger.debug(m)
    return (0, out)


def gitfetch_cmd(config):
    os.chdir(config['git_path'])
    _logger.debug(os.getcwd())
    fetch_cmd = ['git', 'fetch', '-v', config['remote_respo']]
    result = 1
    (result, out) = shellCmd(fetch_cmd)
    if result == 1:
        return 1
    return (result, out)


def git_log_cmd(config, diff_id):
    os.chdir(config['git_path'])
    fetch_cmd = ['git', 'log', diff_id]
    result = 1
    (result, out) = shellCmd(fetch_cmd)
    if result == 1:
        return 1
    return (result, out)


def check_update(config):
    update = False
    result, out = gitfetch_cmd(config)

    if result != 0:
        update = False
    else:
        msg = ''
        for line in out.split('\n'):
            if line.find(config['remote_respo']) > 0:
                branch = line.split('/')[1]
                if line.find('up to date') == -1:
                    update = True
                    msg = '\n[' + branch + '] ' + \
                        '分支有更新, commit信息如下\n'
                    diff_id = line.split()[0]
                    msg += logby_diffid(config, diff_id)
                    out = msg

    _logger.info(out)
    return (result, update, out)


def logby_diffid(config, diff_id):
    os.chdir(config['git_path'])
    msg = ''
    msg += 15 * '=' + 'git log ' + diff_id + 15 * '=' + '\n'
    msg += git_log_cmd(config, diff_id)[1]
    msg += 50 * '='
    return msg


def Notice(config, msg):

    content = ''
    content += '[Project]: ' + config['Project_name'] + '\n'
    content += '[server address]:%s\n' % config['server_address']
    content += msg + '\n'
    content += '''

=================================================
这是一封自动转发的邮件，用来通知大家服务器是否有更新，
如果有任何问题，请联系智刚。
=================================================
    '''
    send_mail(config['mailto_list'], config[
              'Project_name'] + u"代码有更新", content)

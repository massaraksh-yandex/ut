from platform.commands.endpoint import Endpoint
from platform.statement.create import create
from platform.utils.utils import register_commands
from platform.params.params import Params
from platform.execute.run import Run
import json
import time


class Wait(Endpoint):
    def name(self):
        return 'wait'

    def _about(self):
        return '{path} - ждёт пока джоба в дженкинсе завершится и печатает её статус'

    def _rules(self):
        return create('Аргументом передаётся адрес сборки').single_option_command(self._wait)

    def _wait(self, p: Params):
        url = p.targets[0].value

        console = '/console'
        if url.endswith(console):
            url = url[:-len(console)]

        while True:
            cmd = Run().cmd("curl -sk '{0}'".format(url+'/api/json')).call()

            try:
                resp = json.loads(cmd)
            except:
                print(cmd)
                return

            if not bool(resp['building']):
                print('сборка {u} завершилась с результатом `{r}`'.format(u=url, r=resp['result']))
                break

            time.sleep(5)


commands = register_commands(Wait)

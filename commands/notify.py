from platform.commands.endpoint import Endpoint
from platform.statement.create import create
from platform.statement.rule import Rule
from platform.utils.utils import register_commands
from platform.params.params import Params
import urllib.request
import urllib.parse
import socket


class Notify(Endpoint):
    def name(self):
        return 'ntf'

    def _about(self):
        return '{path} - посылает сообщение в тг от имени бота'

    def _rules(self):
        return create('Аргументом передаётся сообщение').extended()\
            .statement('Любое количество аргументов', result=self._notify, rule=Rule())\
            .product()

    def _notify(self, p: Params):
        key = '249099545:AAH5OB-N0nch1nV65Td3GWwaCzFZLgLKbXM'
        args = {
            'chat_id': '103645045',
            'text': '*{host}*: {msg}'.format(host=socket.gethostname(), msg=' '.join(p.argv)),
            'parse_mode': 'Markdown'
        }

        url = 'https://api.telegram.org/bot{key}/sendMessage?{args}'.format(key=key,
                                                                            args=urllib.parse.urlencode(args))

        req = urllib.request.Request(url=url.format(**args))
        with urllib.request.urlopen(req):
            pass


commands = register_commands(Notify)

import argparse
from .constants import *

class ArgumentParserRunner:
    def __init__(self):        
        self.parser = argparse.ArgumentParser(conflict_handler='resolve') 
        self.group = self.parser.add_argument_group('QUIC verification with Ivy')
        self.group.add_argument(
            '--mode', 
            help='Mode of experiments - "client" vs "server" (default)',
            type=str, 
            default="server"
        )
        
        self.group.add_argument(
            '--implementations', 
            help='Implementations tested ('+ str([*IMPLEMENTATIONS])  +') (default: all)',
            type=str, 
            nargs='+',
        )
        self.group.add_argument(
            '--dir', 
            help='Output directory to create (default: temp/)',
            type=str, 
            default=None
        )
        self.group.add_argument(
            '--iter', 
            help='Number of iteration per test (default: 1)',
            type=int, 
            default=1
        )
        self.group.add_argument(
            '--nclient', 
            help='Number of client per test for server implementation (default: 1)',
            type=int, 
            default=1
        )
        self.group.add_argument(
            '--getstats', 
            help='Print all stats (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--compile', 
            help='Compile Ivy tests (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--run', 
            help='For server/client test, launch or not the server/client (default:True)',
             action="store_false"
        )
        self.group.add_argument(
            '--timeout', 
            help='Timeout (default: 100 sec)',
            type=int, 
            default=100
        )
        self.group.add_argument(
            '--gdb', 
            help='Use gdb to debug (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--keep_alive', 
            help='Keep alive Ivy implementation (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--update_include_tls', 
            help='Update <include> folder for picoTLS files of Ivy (defined by g++) (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--docker', 
            help='Use docker (default:False)',
            action="store_true"
        )
        self.group.add_argument(
            '--alpn', 
            help='alpn (default: hq-29)',
            type=str, 
            default="hq-29"
        )
        self.group.add_argument(
            '--categories', 
            help='Categories of tests considered (default: all)',
            type=str, 
            default="all"
        )
       
        
    def parse_arguments(self, allow_unk=False):
        args = None
        if not allow_unk:
            args = self.parser.parse_args() 
        else:
            args, unknown = self.parser.parse_known_args()
        return args

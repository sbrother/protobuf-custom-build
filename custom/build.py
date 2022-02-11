import setuptools
from distutils import log
import os
import subprocess

class Command(setuptools.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        log.info("Building protobufs NOW again...")
        import protoletariat.rewrite
        all_protos = [f for f in setuptools.findall() if f.endswith('.proto')]
        subprocess.run(['protoc', '--python_out=proto', '-Iproto'] + all_protos, check=True)

        all_pb2 = [f for f in setuptools.findall() if f.endswith('pb2.py')]
        log.info(f"All pb2 {', '.join(all_pb2)}")

        subprocess.run(['protol', '--create-package', '--in-place',
                        '--python-out', 'proto', 'protoc',
                        f'--proto-path=proto'] + all_protos,
                       check=True)

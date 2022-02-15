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
        log.info("Running protobuf compilation step...")
        all_protos = [f for f in setuptools.findall() if f.endswith('.proto')]
        if not all_protos:
            return

        log.info(f"Compiling protos in {os.path.commonpath(all_protos)}...")
        subprocess.run(['protoc', '--python_out=.'] + all_protos, check=True)

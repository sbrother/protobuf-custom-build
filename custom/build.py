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
        log.info("Running protobuf compilation...")
        all_protos = [f for f in setuptools.findall() if f.endswith('.proto')]
        if not all_protos:
            return

        root_dir = os.path.commonpath(all_protos)
        log.info(f"Compiling protos in {root_dir}...")
        subprocess.run(['protoc', '--python_out=' + root_dir, '-I' + root_dir]
                       + all_protos, check=True)

        log.info(f"Running protoletariat to fix imports...")
        subprocess.run(['protol', '--create-package', '--in-place',
                        '--python-out', root_dir, 'protoc',
                        f'--proto-path={root_dir}'] + all_protos,
                       check=True)

import setuptools
from distutils import log


class Command(setuptools.Command):
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        log.info("Building protobufs...")


#------------------------------------------------------------------------
# Copyright (c) 2015 SGW
#
# Distributed under the terms of the New BSD License.
#
# The full License is in the file LICENSE
#------------------------------------------------------------------------

# Use setuptools to recognize the install_requires option.
from setuptools import setup

import os
import subprocess

MAJOR = 0
MINOR = 0
MICRO = 1
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR,MINOR,MICRO)

# Return the git revision as a string
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout = subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION

def get_version_info():
    # Adding the git rev number needs to be done inside
    # write_version_py(), otherwise the import of scipy.version messes
    # up the build under Python 3.
    FULLVERSION = VERSION
    if os.path.exists('.git'):
        GIT_REVISION = git_version()
    elif os.path.exists('velvet/version.py'):
        # must be a source distribution, use existing version file
        # load it as a separate module to not load velvet/__init__.py
        import imp
        version = imp.load_source('velvet.version', 'velvet/version.py')
        GIT_REVISION = version.git_revision
    else:
        GIT_REVISION = "Unknown"

    if not ISRELEASED:
        FULLVERSION += '.dev-' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


def write_version_py(filename='velvet/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM VELVET SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    FULLVERSION, GIT_REVISION = get_version_info()

    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'full_version' : FULLVERSION,
                       'git_revision' : GIT_REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()


def setup_package():

    # Rewrite the version file everytime
    write_version_py()

    setup(name='velvet',
        version=VERSION,
        author='SGW',
        author_email='sgwoodjr@gmail.com',
        url='https://github.com/sgwoodjr/velvet',
        packages=['velvet','velvet.test'],
        license = 'LICENSE',
        description='Beautiful signal processing and communications algorithms in Python',
        long_description=open('README.rst').read(),
        keywords="signal processing, communications, DSP",
        install_requires=[],
        setup_requires=[],
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Science/Research",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: Implementation",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Scientific/Engineering",
            ],
    )


if __name__ == '__main__':
    setup_package()

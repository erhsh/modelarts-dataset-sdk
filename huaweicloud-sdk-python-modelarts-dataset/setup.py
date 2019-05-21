# Copyright 2018 Deep Learning Service of Huawei Cloud. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import re

import setuptools
from setuptools import setup

PACKAGE_NAME = 'huaweicloud-sdk-python-modelarts-dataset'

with open('README.md') as f:
    long_description = f.read()

with io.open('modelarts/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)
    if version is None:
        raise ImportError('Could not find __version__ in modelarts/__init__.py')

REQUIRED_PACKAGES = [
    'esdk-obs-python>=3.0.5'
]

EXTRA_REQUIRE = {
    # `docs` versions are to facilitate local generation of documentation.
    # Sphinx 1.3 would be desirable, but is incompatible with current ATG setup.
    # Thus the pinning of both sphinx and alabaster versions.
    'docs': [
        'sphinx==1.2.2',
        'alabaster==0.7.11'
    ],
    'opencv': ['opencv-python>=3.2.0.6'],
    'tf': ['tensorflow>=1.4.0'],
    'tf_gpu': ['tensorflow-gpu>=1.4.0'],
    'test': [
        'Pillow>=3.0',
        'codecov>=2.0.15',
        'mock>=2.0.0',
        'opencv-python>=3.2.0.6',
        'flake8',
        'pylint>=1.9',
        'pytest>=3.0.0',
        'pytest-cov>=2.5.1',
        'pytest-forked>=0.2',
        'pytest-logger>=0.4.0',
        'pytest-timeout>=1.3.3',
        'pytest-xdist',
        's3fs>=0.0.1',
    ],
    'torch': ['torchvision>=0.2.1'],
}

packages = setuptools.find_packages()

setup(
    name=PACKAGE_NAME,
    version=version,
    install_requires=REQUIRED_PACKAGES,
    packages=packages,
    description='huaweicloud-sdk-python-modelarts-dataset.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License, Version 2.0',
    extras_require=EXTRA_REQUIRE,
    entry_points={
    },
    url='https://github.com/huawei-clouds/modelarts-dataset-sdk',
    author='Huawei Technologies, Inc.',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)

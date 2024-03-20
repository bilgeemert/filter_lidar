from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'filter_scan'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bilge',
    maintainer_email='bilgenurmert@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'filter_scan_node=filter_scan.angle_filter:main',
            'distance_node=filter_scan.distance_filter:main',
            
        ],
    },
)

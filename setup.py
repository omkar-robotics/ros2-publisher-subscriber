from setuptools import setup

package_name = 'my_pubsub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omi',
    maintainer_email='omi@todo.todo',
    description='ROS2 publisher subscriber example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = my_pubsub_pkg.publisher:main',
            'subscriber = my_pubsub_pkg.subscriber:main',
        ],
    },
)

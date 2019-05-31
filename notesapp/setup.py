from setuptools import setup

setup(
    name = 'notes',
    version = '0.1.0',
    packages = ['notesapp'],
    install_requires=[ 'plumbum', ],
    entry_points = {
        'console_scripts': [
            'notes = notesapp.__main__:Notes',
                    ]
    })
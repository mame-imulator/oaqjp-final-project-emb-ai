# setup.py
from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
#    description='Emotion detection using IBM Watson NLP service',
#    author='Your Name',
#    author_email='your.email@example.com',
#    python_requires='>=3.6',
)

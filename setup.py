from setuptools import setup, find_packages
import os
import subprocess
import setuptools.command.install

class PostInstallCommand(setuptools.command.install.install):
    def run(self):
        subprocess.check_call([os.sys.executable, 'post_install.py'])
        setuptools.command.install.install.run(self)

setup(
    name='processpdfdocs',
    version='0.0.9',
    packages=find_packages(),
    install_requires=[
        "vietocr==0.3.13",
        "opencv-contrib-python==4.6.0.66",
        "PyMuPDF==1.24.5",
        "pdf2image==1.17.0",
        "pdftotext==2.2.2",
        "numpy==1.26.4",
        "pillow==10.2.0",
        "ultralytics==8.0.239",
        "onnxruntime",
        "paddleocr==2.7.3",
        "paddlepaddle==2.6.1"
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)
from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='nbtransom',
      version='1.0.1',
      description='Machines and people collaborating together through Jupyter notebooks.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
      ],
      keywords='human-in-the-loop, active learning, collaborative documents, jupyter notebook, pipelines, machine learning',
      url='http://github.com/ceteri/nbtransom',
      author='Paco Nathan',
      author_email='ceteri@gmail.com',
      license='Apache License 2.0',
      packages=['nbtransom'],
      install_requires=[
          'nbformat',
          'pandas',
      ],
      zip_safe=False)

from distutils.core import setup

setup(
    name = 'Pyroscope',         # Package name
    packages = ['Pyroscope'],   
    version = '0.1',      # Initial version
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Data fusion package for transforming L2 satellite to L3 spatial-temporal gridded data',  
    author = 'Sally Zhao, Neil Gutkin',                 
    author_email = 'xhaosally0@gmail.com',     
    url = 'https://github.com/jwei-openscapes/aerosol-data-fusion',   # github repository
    download_url = 'NA',   
    keywords = ['data fusion', 'satellite', 'L2', 'L3'],   # Keywords
    install_requires=[            
            'numpy',
            'joblib',
            'cuda',
            'netCDF4',
            'pyhdf',
            'pyyaml'
        ],
    classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers, scientist, researchers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #supported versions
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)
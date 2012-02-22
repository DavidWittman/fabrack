# Fabrack
A Fabric task library for use with Rackspace Cloud Servers. Inspired by Gareth Rushgrove's [cloth](https://github.com/garethr/cloth).

## Installation
This package is meant to be installed using python-setuptools. You can clone this repository and run `python setup.py install`, or take the easy way out and use pip:

`pip install git+git://github.com/DavidWittman/fabrack.git`

## Getting Started
After installation, simply import the functions defined in `fabrack.tasks` to your fabfile in order to begin using Fabrack.

``` python
#!/usr/bin/env python
from fabrack.tasks import *
```

That is pretty much it for the setup. You can now generate and use server lists pulled directly from the Rackspace Cloud API. Fabrack works by generating and saving a list of servers locally so that subsequent requests need not use the API. To generate your first server list, run `fab generate` and enter in your username and API key when prompted. Alternatively, you can pass these values in as parameters on the command line:

```
# fab generate:user=example,apikey=1baabb5ca739bedead7d3beef3c8aa3a

Done.
```

```
# fab match:"^dev-" list
[184.106.x.x] Executing task 'list'
184.106.x.x  dev-web-01
184.106.x.x	dev-web-02
50.57.x.x dev-web-03
50.57.x.x	dev-db-01
```

More to come.

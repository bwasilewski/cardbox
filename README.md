# CardBox

TODO: Write a project description

## Installation

1. Setup virtualenv and Flask

```
$ sudo pip install virtualenv
$ mkdir cardbox
$ cd cardbox
$ virtualenv .
$ . bin/activate
$ pip install Flask
```

2. Pull down this repo in the 'cardbox' directory.
3. Install PyMongo

```
$ pip install Flask-PyMongo
```

4. Add PyMongo in cardbox/application.py

```
from flask import Flask
from flast.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
```

5. Get started!



## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license

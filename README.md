# CardBox

TODO: Write a project description

## Initial Setup

```
$ sudo pip install virtualenv
```

With virtualenv and mongodb installed:

```
$ virtualenv cardbox
$ cd cardbox
$ . bin/activate
$ git clone https://github.com/bwasilewski/cardbox
$ mv cardbox/manage.py . (working on the structure to eliminate this step)
$ cd cardbox
$ pip install -r requirements.txt
```

In a separate tab in same virtualenv:

```
$ mongod (starts mongo server)
```

Back in virtualenv directory:

```
$ python manage.py runserver
```

Leaving the old instructions here until we verify the new setup steps:
```
$ sudo pip install virtualenv
$ mkdir cardbox
$ cd cardbox
$ virtualenv .
$ . bin/activate
$ pip install Flask
$ pip install mongo
$ pip install Flask-PyMongo
$ pip install flask-mongoengine
$ mongod

```

In a separate window, pull down this repo in the 'cardbox' directory.
Get started!

## Usage
From directory above repo, activate virtual environment

```
$ . bin/activate
```

Start the server

```
$ python manage.py runserver
```

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

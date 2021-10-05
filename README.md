# Realtime Database Dump #

This tool dump the full database or any child of the any Firebase Realtime database

## Usage

```python

firebasedump -- utility for dump data from Firebase database

Usage:
  firebasedump  (-d <database> -c <credentials>) <dbtarget> 
  firebasedump  [--verbose] (-d <database> -c <credentials>) <dbtarget> [<output>]
  firebasedump -h | --help
  firebasedump -v | --version

Options:
  -h --help                     Show help screen.
  -v --version                  Show version.
  -d db, --database db          Url path of your database
  -c cd, --credentials cd       Path of your credentials (json file)
  -s, --verbose                 Enable logs
  dbtarget                      Database target path for dump i.e: /users

``` 

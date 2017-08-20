
The Database class
==================

.. post:: 19 June 2013
   :author: Simon Liedtke
   :tags: student, progress, database
   :category: GSoC

Note: I have also a private blog which covers more advanced topics.
The next post there will be about implementing custom caches and custom commands.

The class Database is the central class of the new database package.
It is used to connect to a database and to manipulate it (adding new entries, editing exisitng entries, removing entries).
Later on, it will also be possible to search for entries by specific criteria (I think about using the sunpy.net.vso.attrs module for querying the database).

Connecting, adding entries, getting all entries and checking for existence
--------------------------------------------------------------------------

To connect to a database, you create a new instance of the class Database.
Its __init__ method receives only one positional argument: the URL.
You may either pass a string of the form dialect+driver://user:password@host/dbname[?key=value..] or an instance of the class sqlalchemy.engine.url.URL.
The special string 'sqlite:///:memory:' means that an in-memory SQLite database is used (which is especially handy in interactive session for trying things out).
See sqlalchemy.create_engine for more information about the syntax of the passed string.

The method create_tables is mandatory for working with a new database.
Missing tables are not automatically created because “explicit is better than implicit”.

Each instance of the class DatabaseEntry represents one row in the database.
To add a new entry to the database, simply use the add method of a database object and pass it the entry you want to add.
To check if it exists in the database, you can use the in operator.
The number of entries can be accessed by using the len() function on any database object.
It is also supported to iterate over a database object to get all entries.
As a side-effect, using the list() function on a database object gives you a list of all entries.

::

    from sunpy.database import Database, DatabaseEntry
    >>> database = Database('sqlite:///:memory:')
    >>> database.create_tables()
    >>> entry1 = DatabaseEntry()
    >>> entry2 = DatabaseEntry()
    >>> database.add(entry1)
    >>> database.add(entry2)
    >>> len(database)
    2
    >>> assert entry1 in database
    >>> assert entry2 in database
    >>> pprint(list(database))
    [<DatabaseEntry(id 1, data provider None, fileid None)>,
     <DatabaseEntry(id 2, data provider None, fileid None)>]


When are changes committed to the database?
-------------------------------------------

There are two answers to this question: Changes may either be committed explicitly or implicitly.
The explicit way is easy: any number of database manipulations is flushed by calling the commit method, i.e. `database.commit()` if the name of the Database instance is called database.

The implicit way is a bit harder to understand: Changes are implicitly committed directly before a command reads from the database.

Each of the following commands is committed as soon as a query to the database is issued:

* add
* edit
* remove
* star
* unstar
* undo / redo

By "query" I mean any function, method or operator that reads from the database.
These are in particular:

* `list(database)`
* `len(database)`
* `database.get_entry_by_id`
* `database.get_starred`
* the `in` operator
* iterating over a database

You don’t have to remember each of these functions.
Just keep in mind that changes to the database are committed as soon as any operation is performed to read from the database.
Later on, more methods and features will be added to read from the database, so that generic rule is more useful than learning a list of operations by heart.

Undoing and redoing actions (also: removing entries)
----------------------------------------------------

The actions `add`, `edit`, `remove`, `star`, and `unstar` can be undone and redone using the methods undo or redo, respectively.
Both of these methods receive an optional argument to specify the number of commands that should be undone or redone (the default is 1, i.e. undo or redo only one command).
If the given number of commands cannot be reverted (e.g. if only 2 actions have been undone, it is not possible to redo 5 actions), an exception is raised.

The `remove` method is as simple as the `add` method: you pass an entry and it gets removed.

::

    >>> database.remove(entry1)
    >>> database.remove(entry2)
    >>> list(database)
    []
    >>> database.undo(2)
    >>> pprint(list(database))
    [<DatabaseEntry(id 1, data provider None, fileid None)>,
     <DatabaseEntry(id 2, data provider None, fileid None)>]
    >>> database.redo()
    >>> list(database)
    [<DatabaseEntry(id 2, data provider None, fileid None)>]


Editing entries: (un-)starring entries and custom edits
-------------------------------------------------------

The database package brings the new concept of starring entries.
This is just to mark certain entries, it is not a ranking or a custom label (though while I’m writing this, I think that could be a good idea.
I should discuss it with the SunPy devs).
To star an entry, call the method star and pass the entry to be starred.
The method unstar works accordingly.
If you try to mark an entry as starred although it already is, an exception is raised.
An exception is also raised if it is attempted to unstar an entry that is not starred.
This “verbose” behaviour can be turned off by setting the optional keyword argument `ignore_already_starred` (or `ignore_already_unstarred` for the `unstar` method) to True.
The entry method makes it possible to change a specific value of an entry.
The first argument is the entry to be changed and all following arguments must be keyword arguments where the key represents the column name in the database and the value represents the new value.

::

    >>> database.star(entry2)
    >>> database.get_starred()
    <generator object <genexpr> at 0xb54d734>
    >>> list(database.get_starred())
    [<DatabaseEntry(id 2, data provider None, fileid None)>]
    >>> database.unstar(entry2)
    >>> list(database.get_starred())
    []
    >>> database.edit(entry2, id=42, starred=True)
    >>> list(database.get_starred())
    [<DatabaseEntry(id 42, data provider None, fileid None)>]

Caching
-------

The database may be used as a cache.
In fact, a cache is always used, but the default size is `float('inf')`, meaning infinite size.
There are different possible types of caches and they mainly differ in the way what items they remove if the cache has reached the full size and another item is added.
The default cache is an LRU (Least Recently Used) cache.
This one removes the item where the access time is the oldest.
There is also one other builtin cache, the LFU (Least Frequently Used) cache.
This one removes the entry where the number of accesses is the lowest.
It is also possible to add custom cache algorithms, this will be covered in one of the next posts in my private blog.

The cache type is the second argument, defaulting to sunpy.database.caching.LRUCache.
The cache size of a database is specified by passing the keyword argument cache_size in the `__init__` method.
To get an entry by its unique ID, you use the method `get_entry_by_id`.
In the following example, you can see (at least I hope you do ^^) that the entries #1 and #3 have been accessed once, whereas #2 has not been accessed at all.
So you could imagine that its last accessed time is minus infinity and therefore it gets removed when entry #4 is added to the database.

::

    >>> from pprint import pprint
    >>> database = Database('sqlite:///:memory:', cache_size=3)
    >>> database.create_tables()
    >>> entry1 = DatabaseEntry()
    >>> entry2 = DatabaseEntry()
    >>> entry3 = DatabaseEntry()
    >>> entry4 = DatabaseEntry()
    >>> database.add(entry1)
    >>> database.add(entry2)
    >>> database.add(entry3)
    >>> pprint(list(database))
    [<DatabaseEntry(id 1, data provider None, fileid None)>,
     <DatabaseEntry(id 2, data provider None, fileid None)>,
     <DatabaseEntry(id 3, data provider None, fileid None)>]
    >>> database.get_entry_by_id(1)
    <DatabaseEntry(id 1, data provider None, fileid None)>
    >>> database.get_entry_by_id(3)
    <DatabaseEntry(id 3, data provider None, fileid None)>
    >>> database.add(entry4)
    >>> pprint(list(database))
    [<DatabaseEntry(id 1, data provider None, fileid None)>,
     <DatabaseEntry(id 3, data provider None, fileid None)>,
     <DatabaseEntry(id 4, data provider None, fileid None)>]

What are the next plans?
------------------------

The next big plans are writing actual tables (the current DatabaseEntry class can be seen as a dummy model for now), support querying and adding a connection to the VSO interface so that downloaded data gets automatically added to the database.

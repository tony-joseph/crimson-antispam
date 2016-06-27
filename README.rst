================
Crimson Anti-spam
================

Crimson Anit-spam is an anti-spam package for django framework.

------------------------------------
Requirements
------------------------------------

Crimson antispam supports python versions 2.7, 3.3, 3.4 and 3.5. Django 1.7,
1.8 and 1.9 are supported out of the box. Crimson antispam requires django
migrations hence it will not work on django versions prior to 1.7

------------
Installation
------------

Installation via pip
--------------------

pip is the recommended way of installing python packages. If you do not have
pip installed on your system, please refer to to pip documentation for
information on installing pip. Run the following command from a terminal to
install the current version of crimson anti-spam.

::

    pip install crimson_antispam --upgrade

It is possible to separately install crimson_antispam for python 2 and python
3. Replace pip with pip2 or pip3 depending on your python version.

Installing a development version from github
--------------------------------------------

If you need the latest development version, you can install it from github.
Note that the development version is unstable and may contains bugs. Use the
command below to install development version.

::

    pip install git+https://github.com/tony-joseph/crimson_antispam.git@master

Manual Installation
-------------------

If you want to download and install manually, you can download the latest
version from the following link.

`<https://pypi.python.org/pypi/crimson_antispam/>`_

Adding to django project
------------------------

Crimson antispam must be included in installed apps before using it in a django
project. Open your settings file and add 'antispam' to the list of installed
apps.

::

    INSTALLED_APPS = [
	    ……………
	    'antispam',
	    ……………
    ]

You should run the migrations command to create database tables for antispam.

::

    python manage.py migrate

------------------------------
Working With Spam IP Addresses
------------------------------

Crimson antispam uses a spam IP address database to identify spam. The modal
for this database is located at antispam.models.SpamIP. The antispam package
gives you helper functions to manage this database so that you will never have
to access the SpamIP model directly.

Adding a new IP address to spam list
------------------------------------

Crimson antispam provides a convenient helper function to add an IP to spam
list. Import the add_spam_ip function from helpers.

::

    from antispam.helpers import add_spam_ip

The add_spam_ip function takes an IPv4 or IPv6 IP address as its only argument.
For example

::

    add_spam_ip('192.168.0.1')

The IP address will be added to the spam list if it is not already there. No
error will be produced if it is already in spam list.

Adding a list of addresses to spam list
---------------------------------------

Just like adding a single IP address to spam list, you could also add a list
(or tuple) of IP addresses to spam list. The helpers module has a
bulk_add_spam_ip function for this purpose.

::

    from antispam.helpers import bulk_add_spam_ip
    bulk_add_spam_ip(['192.168.0.1', '192.168.0.2', '192.168.0.3'])

Checking an IP address is in spam list
--------------------------------------

The is_spam_ip function in helpers module checks the given IP address is in
spam list or not. This function takes an IPv4  or IPv6 address as its only
argument. It will return True if the IP address is in spam list and False
otherwise.

::

    from antispam.helpers import is_spam_ip
    is_spam_ip('192.168.0.1')

Removing an IP address form spam list
-------------------------------------

You can remove an IP address from spam list using the remove_spam_ip function
in helpers module. It will remove the IP address if it exists. No error message
will be produced if the IP address is not in the list.

::

    from antispam.helpers import remove_spam_ip
    remove_spam_ip('192.168.0.1')

Managing spam IP list using admin interface
-------------------------------------------

You can use the django admin interface to manage spam IPs. It will be located
as 'Spam ips' under the antispam app.

Importing and exporting spam IP addresses
-----------------------------------------

To export all the spam IP addresses into a csv file, run the following command

::

    python manage.py exportspamips

You can also import spam IP addresses from a csv file. Run the following
command to import IP addresses from csv file into database.

::

    Python manage.py importspamips <csv_file>

csv_file should be the absolute path to the csv file containing spam IP
addresses.

-------------------------
Restricting Spam Requests
-------------------------

Using crimson anti-spam you can block requests from known spam IP addresses and
throttle requests from an IP address if it exceeds the permitted requests per
second.

Blocking spam IP addresses
--------------------------

Blocking using decorator
````````````````````````

Crimson anti-spam provides a block_spam_ip view decorator to block spam IP
addresses from accessing a particular view. Import it as follows

::

    from antispam.decorators import block_spam_ip

Blocking using middleware
`````````````````````````

To block all requests from known spam IP addresses, you can use the
BlockSpamIPMiddleware middleware. Add this middleware to your middleware
classes as follows

::

    MIDDLEWARE_CLASSES = [
        …………………………….
        'antispam.middlewares.BlockSpamIPMiddleware',
        …………………………….
    ]

Blocking in templates
`````````````````````

The crimson anti-spam provides an is_spam_ip template context variable if you
add the antispam_processor to your template context processors. The value of
this variable will be true if the request IP addresses is in spam IP list. Add
the following line to your template context processor settings

::

    'antispam.context_processors.antispam_processor'

You can check spam ip address in template as follows.

::

    {% if is_spam_ip %}
        You are spam
    {% else %}
        You are not spam
    {% endif %}

Throttling requests
-------------------

With crimson anti-spam, you can restrict the number of requests from an IP
address if the requests are happening in quick succession. The default time
difference required between two requests is 1000 milliseconds.  You can
override it in your settings as follows

::

    ANTISPAM_SETTINGS = {
        'REQUEST_INTERVAL': 1000,
    }

For throttling requests, you can either use the view decorator or the
middleware.

Throttling using view decorator
```````````````````````````````

To throttle requests to a particular view, you can use the throttle_requests
view decorator. Import it as follows

::

    from antispam.decorators import  throttle_requests

Throttling using middleware
```````````````````````````

You can throttle requests to all views by adding the ThrottleRequestsMiddleware
to you middleware classes.

::

    MIDDLEWARE_CLASSES = [
        ……………………………
        'antispam.middlewares.ThrottleRequestsMiddleware',
        ……………………………
    ]

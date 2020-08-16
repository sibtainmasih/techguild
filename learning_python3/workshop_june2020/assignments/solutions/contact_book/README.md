Contact Book Application
------------------------

> Disclaimer: This is not a complete solution. It is just for guidance purpose.

Before using Contact Book App, execute following for SQLite DB setup.

```unix
$ python contact_book setup
```

## Add a Client Contact

```unix
$ python3 contact_book add -n Daniel -a "Broadway 16" -c "New Jersey" -p "+1 9862223213" -e "daniel@gmail.com"
```

## Search Client Contacts

Search by name -

```unix
$ python contact_book search -k name -v Daniel[2020-08-16 08:57:02,971][DEBUG][root] Arguments = Namespace(handler_func=<function search_contacts at 0x7fc66f2e6af0>, search_field='name', search_field_value='Daniel')
------  -----------  ----------  -------------  ----------------  -------------------  -------------------
Daniel  Broadway 16  New Jersey  +1 9862223213  daniel@gmail.com  2020-08-16 03:26:26  2020-08-16 03:26:26
------  -----------  ----------  -------------  ----------------  -------------------  -------------------
```

Search by City - 

```unix
$ python contact_book search -k city -v "New Jersey"
[2020-08-16 08:57:50,364][DEBUG][root] Arguments = Namespace(handler_func=<function search_contacts at 0x7f0740b69af0>, search_field='city', search_field_value='New Jersey')
------  -------------------  ----------  -------------  ----------------  -------------------  -------------------
James   Little India Street  New Jersey  +1 986462010   james@gmail.com   2020-08-16 03:25:49  2020-08-16 03:25:49
Daniel  Broadway 16          New Jersey  +1 9862223213  daniel@gmail.com  2020-08-16 03:26:26  2020-08-16 03:26:26
------  -------------------  ----------  -------------  ----------------  -------------------  -------------------
```
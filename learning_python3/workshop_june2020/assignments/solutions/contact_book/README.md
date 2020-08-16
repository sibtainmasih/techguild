Contact Book Application
------------------------

> Disclaimer: This is not a complete solution. It is for reference purpose only.

Before using Contact Book App, execute following for SQLite DB setup.

```unix
$ python contact_book setup
```

### Add a Client Contact

```unix
$ python3 contact_book add -n Daniel -a "Broadway 16" -c "New Jersey" -p "+1 9862223213" -e "daniel@gmail.com"
```

### Update Client Notes

```unix
$ python contact_book update -k name -v Daniel -f notes -n "Interested in Jio stake"
```

### Search Client Contacts

#### Search by name -

```unix
$ python contact_book search -k name -v Daniel
Name    Address      City        Phone          Email             Create Date          Last Modified        Notes
------  -----------  ----------  -------------  ----------------  -------------------  -------------------  -----------------------
Daniel  Broadway 16  New Jersey  +1 9862223213  daniel@gmail.com  2020-08-16 03:26:26  2020-08-16 03:52:30  Interested in Jio stake
```

#### Search by City - 

```unix
$ python contact_book search -k city -v "New Jersey"
Name    Address              City        Phone          Email             Create Date          Last Modified        Notes
------  -------------------  ----------  -------------  ----------------  -------------------  -------------------  -----------------------
James   Little India Street  New Jersey  +1 986462010   james@gmail.com   2020-08-16 03:25:49  2020-08-16 03:25:49
Daniel  Broadway 16          New Jersey  +1 9862223213  daniel@gmail.com  2020-08-16 03:26:26  2020-08-16 03:52:30  Interested in Jio stake
```

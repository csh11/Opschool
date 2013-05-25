#!/usr/bin/python



############################
#Modules                   #
############################


try:
    import re
    import os
    import sqlite3 as lite
    import sys 

except ImportError:
    print 'There is a missing module, Please check all modules'
    sys.exit(1)




######################
#Opschool            #
######################

def opinto():
    con = lite.connect('/var/trac/dev/db/trac.db', isolation_level=None)
    with con:
        cur = con.cursor()
        os.chdir('/var/trac/sysadmin/pydoc/opschool')
        dirEntries = os.listdir('/var/trac/sysadmin/pydoc/opsschool')
        for entry in dirEntries:
            if re.match("^index", entry):
                with open (entry) as f:
                    opintro = f.read()
                    cur.execute("insert into wiki
                    (name,version,time,author,ipnr,text,comment,readonly) values
                    (?,?,?,?,?,?,?,?)",
                    ('\r\n[[wiki:Introduction]]\r\n','2','','opschool','','\r\n=introduction=\r\n'
                        + opintro,'',''))
                    cur.close()




                   




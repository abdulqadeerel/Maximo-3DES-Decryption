# Maximo-3DES-Decryption
Breaking down Maximo's 3DES password encryption in DB2


IBM Maximo stores user passwords in DB2 as 3DES-CBC encrypted binary values. In this post I'll show how to decrypt them using a Maximo Automation Script written in Jython — without any external libraries


Usage: 
It can be used as a Action Launch Point to be assigned to a Push Button, or an Action in the Maxuser application.

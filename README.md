# Maximo-3DES-Decryption
Breaking down Maximo's 3DES password encryption in DB2


IBM Maximo stores user passwords in DB2 as 3DES-CBC encrypted binary values. In this post I'll show how to decrypt them using a Maximo Automation Script written in Jython — without any external libraries

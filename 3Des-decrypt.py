service.error("","Error")
from psdi.server       import MXServer
from psdi.mbo          import DBShortcut
from javax.crypto      import Cipher
from javax.crypto.spec import SecretKeySpec, IvParameterSpec
from java.lang         import String
from jarray            import array

def toJBytes(s):
    return array([b if b < 128 else b - 256 for b in s], 'b')

def decrypt(hexStr):
    s = hexStr.strip()
    if s.upper().startswith("X'") and s.endswith("'"):
        s = s[2:-1]
    KEY = toJBytes([ord(c) for c in "Sa#qk5usfmMI-@2dbZP9`jL3"])
    IV  = toJBytes([ord(c) for c in "beLd7$lB"])
    ct  = toJBytes([int(s[i:i+2], 16) for i in range(0, len(s), 2)])
    c   = Cipher.getInstance("DESede/CBC/PKCS5Padding")
    c.init(Cipher.DECRYPT_MODE, SecretKeySpec(KEY, "DESede"), IvParameterSpec(IV))
    return String(c.doFinal(ct), "UTF-8").toString().replace("\x00", "").strip()

def getHash(loginId):
    dbs = DBShortcut()
    try:
        dbs.connect(MXServer.getMXServer().getSystemUserInfo().getConnectionKey())
        rs = dbs.executeQuery("SELECT HEX(PASSWORD) FROM MAXUSER WHERE LOGINID = '" + loginId + "'")
        val = rs.getString(1) if rs.next() else None
        rs.close()
        dbs.commit()
    finally:
        dbs.close()
    return val

try:
    loginId = mbo.getString("LOGINID")  
    rawHex  = getHash(loginId)
    #mbo.setValue("MEMO", decrypt(rawHex) if rawHex else "No password found", 11L)
    service.error("",decrypt(rawHex))
except Exception as e:
    mbo.setValue("MEMO", "ERROR: " + str(e), 11L)
    
    
    
    
####

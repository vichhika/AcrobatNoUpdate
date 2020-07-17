from os import system
from winreg import ConnectRegistry, CreateKey, DeleteKey, DeleteValue, SetValueEx, HKEY_LOCAL_MACHINE , OpenKey, OpenKeyEx, REG_DWORD
from win32 import win32api
def disablebUpdater():
    try:
        root = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        bUpdater_key = OpenKeyEx(root, r"SOFTWARE\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown")
        SetValueEx(bUpdater_key, "bUpdater", 0, REG_DWORD, 0)
    except OSError:
        bUpdater_key = CreateKey(root, r"SOFTWARE\Policies\Adobe\Adobe Acrobat\DC\FeatureLockDown")
        SetValueEx(bUpdater_key, "bUpdater", 0, REG_DWORD, 0)

    
def disableService():
    system("sc STOP AdobeARMservice && sc CONFIG AdobeARMservice START=DISABLED")
    system("sc STOP AGMService && sc CONFIG AGMService START=DISABLED")
    system("sc STOP AGSService && sc CONFIG AGSService START=DISABLED")
    system("sc STOP AdobeUpdateService && sc CONFIG AdobeUpdateService START=DISABLED")
    
if __name__ == "__main__":
    try:
        disablebUpdater();
        disableService();
        win32api.MessageBox(0, "Done, No more update !. Enjoy crack :)", "AcrobatUpdate", 0x00000000 | 0x00000040 )
    except OSError:
        win32api.MessageBox(0, "Failed, Please run as administrator !", "AcrobatUpdate", 0x00000000 | 0x00000030 )
    
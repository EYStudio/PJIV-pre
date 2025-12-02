import ctypes
import subprocess
import win32gui, win32con


class JIVLogic:
    def __init__(self):
        pass

    @staticmethod
    def is_admin():
        """Checking whether programme has administrator privilege"""

        authority = ctypes.windll.shell32.IsUserAnAdmin()
        return bool(authority)

    @staticmethod
    def get_studentmain_state():
        state = subprocess.run("tasklist|find /i \"studentmain.exe\"", shell=True).returncode
        # print(not state)
        return not state

    @staticmethod
    def set_window_top_most(hwnd):
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST,
                              0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

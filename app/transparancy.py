import win32api
import win32con
import win32gui

from app import Color


def setup(hwnd: Color, alpha_color) -> None:
    """Set the windows in alpha and no-clip mode."""
    win_long = win32gui.GetWindowLong(
        hwnd,
        win32con.GWL_EXSTYLE
    )

    win32gui.SetWindowLong(
        hwnd,
        win32con.GWL_EXSTYLE, win_long | win32con.WS_EX_LAYERED
    )

    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOPMOST,
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
    )

    win32gui.SetLayeredWindowAttributes(
        hwnd,
        win32api.RGB(*alpha_color),
        0,
        win32con.LWA_COLORKEY
    )

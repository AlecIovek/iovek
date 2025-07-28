import base64
from seleniumbase import SB

# Ask the user for base64 input
b_input = 'aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM='
anf = base64.b64decode(b_input)
axf1 = anf.decode('utf-8')
with SB(uc=True, test=True) as ettey:
    url = axf1
    ettey.uc_open_with_reconnect(url, 5)
    ettey.uc_gui_click_captcha()
    ettey.sleep(2)
    ettey.uc_gui_handle_captcha()
    while(ettey.is_element_present('video#video-player')):
        ettey.sleep(10)

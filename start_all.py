import msvcrt
print('path to folder')
user_input = b''

while True:
    pressed_key = msvcrt.getche()  # getch() will not echo key to window if that is what you want
    if pressed_key == b'\x1b':  # b'\x1b' is escape
        raise SystemExit
    elif pressed_key == b'\r':  # b'\r' is enter or return
        break
    else:
        user_input += pressed_key       
def file_command(user_input):
    f = open(filepath, "a+")
    f.write("berry")

a_directory = "dir"
for filename in os.listdir(user_input):
    filepath = os.path.join(user_input, filename)
    file_command(filepath)

import os, platform
if platform.system () == "Windows":
    import msvcrt
def getch() :
    if platform.system() == "Linux":
        os.system("bash -c \"read -n 1\"")
    else:
        msvcrt.getch()

print("Pulsa una tecla!")
getch()
print("Correcto")
    
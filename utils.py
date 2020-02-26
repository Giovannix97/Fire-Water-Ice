import os

def change_directory_to_current_executable():
    """ Find and change the directory that contains the current executable file (Game GUI)"""
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    
def move_to_png_img_directory():
    """ Change directory from home to png images"""
    try:    
        change_directory_to_current_executable()
        os.chdir(os.getcwd() + r"\img\png")
    except Exception:
        print("Error while trying to change directory")


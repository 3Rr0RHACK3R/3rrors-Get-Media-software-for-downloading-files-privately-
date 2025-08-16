import sys
from cx_Freeze import setup, Executable

# The name of our project, professional and to the point.
product_name = "Get-Audio"

# We're building a CONSOLE application now, so the base is None.
# The user needs to interact with the input() function.
base = None

# The magic build options! We tell cx_Freeze which packages to include and what files to copy.
build_exe_options = {
    # This includes the Python packages our software needs.
    "packages": ["pytubefix", "requests", "bs4"],
    
    # This is SUPER important. It tells cx_Freeze to include our LICENSE file
    # and the Setup-first.exe installer we rely on.
    "include_files": ["LICENSE", "installer.exe"],
}

# The main setup function. This is what the cx_Freeze command will run.
setup(
    name=product_name,
    version="1.0",
    description="A professional and reliable audio downloader.",
    options={"build_exe": build_exe_options},
    executables=[Executable("Get-Audio.py", base=base)]
)

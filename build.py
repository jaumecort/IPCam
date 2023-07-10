import os
import shutil

app_name = "IPCam"
data_dirs_paths = [
    '/config',
    ]

project_path = os.getcwd()+'/'
spec_path = project_path+'build/'
dist_path = project_path+app_name+'-dist/'
source_path = project_path+'src'
main_script_name = '/main.py'

if os.path.exists(dist_path):
    shutil.rmtree(dist_path)

# One file installation
os.system('pyinstaller --noconfirm --onefile --windowed --specpath '+spec_path+' --distpath '+dist_path+' --icon "'+project_path+'etc/img/SecurityCamera_icon-icons.com_55219.ico" --name '+app_name+'  --paths "'+source_path+'"  "'+source_path+main_script_name+'"')

# Needed directories
for dir in data_dirs_paths:
    src_path =project_path+dir
    dst_path = dist_path+dir
    shutil.copytree(src_path, dst_path, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)

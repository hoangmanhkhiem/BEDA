import subprocess
import static.router.user as u
import static.router.scripts as s
import static.router.infomation as i

def send_file_to_vm(path_vm, path_file, id):
    try:
        # Get username and password
        VM_USERNAME, VM_PASSWORD = u.getuser_by_id_room(id)
        VM_USERNAME = '"' + VM_USERNAME + '"'
        VM_PASSWORD = '"' + VM_PASSWORD + '"'
        command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN + " -gu " + VM_USERNAME + " -gp " + VM_PASSWORD + " -gu " + VM_USERNAME + " -gp " + VM_PASSWORD + " CopyFileFromHostToGuest " + path_vm + " " + path_file
        subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        print("File sent to VM: " + path_vm)
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))


def send_file_to_all_vm(path_file, room):
    try:
        list_pathvm = i.get_pathvm_by_room(room)
        VM_USERNAME, VM_PASSWORD = u.getuser_by_id_room(room)
        VM_USERNAME = '"' + VM_USERNAME + '"'
        VM_PASSWORD = '"' + VM_PASSWORD + '"'
        for path in list_pathvm:
            path = '"' + path + '"'
            command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN + " -gu" + VM_USERNAME + " -gp " + VM_PASSWORD + " CopyFileFromHostToGuest " + path + " " + path_file
            subprocess.run(command, shell=True, stdout=subprocess.PIPE)
            print("File sent to VM: " + path)
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))
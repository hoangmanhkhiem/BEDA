import static.router.user as u
import static.router.scripts as s
import subprocess

list_process = []

def exce_list_process_in_1vm(path_vm,id):
    try:
        # Get username and password
        VM_USERNAME, VM_PASSWORD = u.getuser_by_id_room(id)
        VM_USERNAME = '"' + VM_USERNAME + '"'
        VM_PASSWORD = '"' + VM_PASSWORD + '"'
        path_vm = '"' + path_vm + '"'
        command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN + " -gu " + VM_USERNAME + " -gp " + VM_PASSWORD + " listProcessesInGuest " + path_vm + " -interactive"
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        listt = process.stdout.splitlines()
        for i in listt:
            list_process.append(i.decode('utf-8'))
        print("Processes running in the guest:")

    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))
        
def find_PID_by_name(name,PATH_VMX):
    VM_USER = '"' + s.VM_USER + '"'
    VM_PASSWORD = '"' + s.VM_PASSWORD + '"'
    PATH_VMX = '"' + PATH_VMX + '"'
    command = s.SCRIPT_CONNECT_TO_SERVER + ' ' + s.PATH_VMRUN + ' -gu ' + VM_USER+ ' -gp '+ VM_PASSWORD+ ' listProcessesInGuest '+ PATH_VMX+ ' -interactive'
    try:    
        process = subprocess.run(command,shell=True,stdout=subprocess.PIPE)
        for line in process.stdout.splitlines():
            if name in str(line):
                n = ""
                for i in str(line.split()[0]):
                    if i.isdigit():
                        n += str(i)
                return n
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Failed to find process with name {name}.")
        return "None"
    
def kill_process_by_name(name,PATH_VMX):
    while True:
        process_id = find_PID_by_name(name)
        if "None" in str(process_id):
            return
        VM_USER = '"' + s.VM_USER + '"'
        VM_PASSWORD = '"' + s.VM_PASSWORD + '"'
        PATH_VMX = '"' + PATH_VMX + '"'
        command = s.SCRIPT_CONNECT_TO_SERVER + ' ' + s.PATH_VMRUN+ '-gu ' + VM_USER+ ' -gp '+VM_PASSWORD+ ' killProcessInGuest ' + PATH_VMX + ' '+ str(process_id)
        try:
            subprocess.run(command, text=True,shell=True,stdout=subprocess.PIPE)
            print(f"Process with ID {process_id} killed.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print(f"Failed to kill process with ID {process_id}.")



def exce_list_process():
    try:
       for i in list_process:
            print(i)
    except:
        return None


def get_list_process():
    return list_process


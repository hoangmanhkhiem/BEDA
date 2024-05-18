import static.router.scripts as s
import static.router.user as u
import static.router.infomation as i
import static.remote.process as p
import subprocess
import json

list_program = []

def load_program_need_check():
    list_program = []
    try:
        with open(s.PATH_PROGRAM, 'r') as f:
            program = json.load(f)
            for key in program:
                k = key['name'], key['link_source'] , key['link_in_vm']
                list_program.append(k)
    except:
        print("Error: Can't load program need check.")

def check_program_installed(room):
    VM_USER, VM_PASSWORD = u.getuser_by_id_room(1)
    PATH_VMX = i.get_pathvm_by_room(room)
    VM_USER = '"' + VM_USER + '"'
    VM_PASSWORD = '"' + VM_PASSWORD + '"'
    PATH_VMX = '"' + PATH_VMX + '"'
    for name_computer in PATH_VMX:
        print(f"Checking program in {name_computer}")
        for program_name,program_path_in_ln, program_path in list_program:
            command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN +  ' -gu ' + VM_USER + ' -gp ' + VM_PASSWORD + ' runProgramInGuest ' + name_computer + ' -noWait ' + program_path   
            try:
                subprocess.run(command,shell=True, capture_output=True, text=True, check=True)
                print(f"{program_name[:-4]} is installed and successfully executed.")
            except subprocess.CalledProcessError as e:
                print(f"{program_name[:-4]} is not installed.")
            program_name = str(program_name)
            while True:
                process_id = p.find_PID_by_name(program_name, name_computer)
                if "None" in str(process_id):
                    break
                command = s.SCRIPT_CONNECT_TO_SERVER + ' ' + s.PATH_VMRUN+ '-gu ' + s.VM_USER+ ' -gp '+ s.VM_PASSWORD+ ' killProcessInGuest ' + name_computer + ' '+ str(process_id)
                try:
                    subprocess.run(command, text=True,shell=True,stdout=subprocess.PIPE)
                except subprocess.CalledProcessError as e:
                    print(f"Error: {e}")
                    
def send_file_to_vm(id,room,link_source,link_in_vm):
    VM_USER, VM_PASSWORD = u.getuser_by_id_room(id)
    PATH_VMX = i.get_pathvm_by_id_and_room(id,room)
    VM_USER = '"' + VM_USER + '"'
    VM_PASSWORD = '"' + VM_PASSWORD + '"'
    PATH_VMX = '"' + PATH_VMX + '"'
    print(f"Sending file to {PATH_VMX}")
    command = s.SCRIPT_CONNECT_TO_SERVER + " " + s.PATH_VMRUN +  ' -gu ' + VM_USER + ' -gp ' + VM_PASSWORD + ' CopyFileFromHostToGuest ' + PATH_VMX + ' ' + link_source + ' ' + link_in_vm
    try:
        subprocess.run(command,shell=True, capture_output=True, text=True, check=True)
        print(f"File is sent successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
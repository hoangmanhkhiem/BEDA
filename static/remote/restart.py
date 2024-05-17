import static.router.scripts as s
import static.router.infomation as i
import subprocess


def restart_all_vm():
    try:
        list_pathvm = i.get_pathvm_by_room()
        # for path in list_pathvm:
        #     # command = s.SCRIPT_CONNECT_TO_SERVER + s.PATH_VMRUN + "reset " + path
        #     # subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        #     # print("Restarting VM: " + path)
        print(list_pathvm)
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))


def restart_vm_by_id(id):
    try:
        path_vm = i.get_all_vmpath()
        for path in path_vm:
            if id in path:
                # command = s.SCRIPT_CONNECT_TO_SERVER + s.PATH_VMRUN + "reset " + path
                # subprocess.run(command, shell=True, stdout=subprocess.PIPE)
                print("OK")
            return "Restarting VM: " + path[0]
    except subprocess.CalledProcessError as e:
        print("Error running command: " + e.cmd)
        print("Return code: " + str(e.returncode))

import configparser

def read_inventory(file_path, host_group, var_patern):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_path)
    if host_group in config:
        for key in config[host_group]:
            with open(file_path, 'r') as file_object:
                line = file_object.readline()
                while line:
                    if line.find(key) == 0:
                        host_var_list = line.split(' ')
                        for index_list in host_var_list:
                            if var_patern in index_list:
                                #print(index_list)
                                ansible_var = index_list.split('=')
                                return ansible_var[1]
                        break
                    line = file_object.readline()
    else:
        return 0
    
# an example
# extract only first host in the group
# 1)path to file, 2)host group, 3)variable
host_ip = read_inventory('inventory.ini', 'mongo', 'ansible_host')
print(host_ip)

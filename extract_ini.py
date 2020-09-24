import configparser

def read_inventory(file_path, host_group, host, var_patern):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_path)
    if host_group in config:
        for key in config[host]:
            with open(file_path, 'r') as file_object:
                line = file_object.readline()
                while line:
                    if line.find(key) == 0:
                        host_var_list = line.split(' ')
                        for index_list in host_var_list:
                            if var_patern in index_list:
                                #print(index_list)
                                ansible_host_ip = index_list.split('=')
                                return ansible_host_ip[1]
                        break
                    line = file_object.readline()
    else:
        return 0
    
# example
host_ip = read_inventory('inventory.ini', 'mongo', 'mongo_host_1', 'ansible_host')
print(host_ip)

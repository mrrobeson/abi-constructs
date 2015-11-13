import abi_config
import abi_sys_file

control_identifier = "A"
current_date = "012215"#raw_input("Enter as of date in the format DDMMYY:")

a_record = "%s%s%s%s%s01" % (control_identifier, abi_config.site_code, abi_config.filer_code, abi_config.com_password, abi_sys_file.sys_date)

while len(a_record) < 80:
    a_record = a_record + " "

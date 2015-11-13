import abi_config
import abi_sys_file

control_identifier = "Z"
current_date = "012215"#raw_input("Enter as of date in the format DDMMYY:")

z_record = "%s%s%s%s%s01" % (control_identifier, abi_config.site_code, abi_config.filer_code, abi_config.com_password, abi_sys_file.sys_date)

while len(z_record) < 80:
    z_record = z_record + " "

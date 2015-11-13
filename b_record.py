import abi_config

control_identifier = "B"
current_date = "012215"#raw_input("Enter as of date in the format DDMMYY:")
app_id = "WI"

b_record = "%s01%s%s%s" % (control_identifier, abi_config.site_code, abi_config.filer_code, app_id)

while len(b_record) < 80:
    b_record = b_record + " "

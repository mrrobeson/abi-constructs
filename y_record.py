import abi_config
import abi_message_constructor

control_identifier = "Y"
current_date = "012215"#raw_input("Enter as of date in the format DDMMYY:")
app_id = "WI"
num_records = len(abi_message_constructor.abi_message) / 80
while len(str(num_records)) < 5:
    num_records = "0" + str(num_records)

y_record = "%s  %s%s%s%s" % (control_identifier, abi_config.site_code, abi_config.filer_code, app_id, num_records)

while len(y_record) < 80:
    y_record = y_record + " "
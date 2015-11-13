import abi_message_constructor
import a_record
import b_record
import y_record
import z_record

header = a_record.a_record + b_record.b_record 
trailer = y_record.y_record + z_record.z_record

abi_file = header + abi_message_constructor.abi_message + trailer

print abi_file

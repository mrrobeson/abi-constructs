hs_too_long_warning = "Tariff number is too long"

control_identifier = 'W'

from_tariff_num = "12345678"
if len(from_tariff_num) > 10:
    print hs_too_long_warning
while len(from_tariff_num) < 10:
    from_tariff_num = from_tariff_num + " "

as_of_date = "220115"#raw_input("Enter as of date in the format DDMMYY:")

to_tariff_num = "8888888888"
if len(to_tariff_num) > 10:
    print hs_too_long_warning
while len(to_tariff_num) < 10:
    to_tariff_num = to_tariff_num + " "

wi_line_w = "%s  %s%s%s" % (control_identifier, from_tariff_num, as_of_date, to_tariff_num)

while len(wi_line_w) < 80:
    wi_line_w = wi_line_w + " "

def get_wi_line_w():
    return wi_line_w
def lastDigit(barcode):
	if len(barcode)!=12:
		return "error:wrong len"
	else:
		control2 = int(barcode[1])+int(barcode[3])+int(barcode[5])+int(barcode[7])+int(barcode[9])+int(barcode[11])
		control1 = int(barcode[0])+int(barcode[2])+int(barcode[4])+int(barcode[6])+int(barcode[8])+int(barcode[10])
		control = 10-(control2*3+control1)%10
		if control == 10:
			control = 0
		return str(control)
			
def getFullBarcode(barcode):
	if len(barcode)!=12:
		return "error:wrong len"
	else:
		return barcode+lastDigit(barcode)

if __name__ == "__main__":
	print("Usage: \ngetFullBarcode('460608610841') and get",getFullBarcode('460608610841'))
	print("Or lastDigit('460608610841') and get",lastDigit('460608610841'))

def final_bill(bill, tip=0.20, tax=0.0675):
	tip_total = bill*tip
	tax_total = bill*tax
	final_bill= bill+tip_total+tax_total
	print "the final_bill is {0}".format(final_bill)
	return final_bill

final_bill(100,0.20,0.0675)

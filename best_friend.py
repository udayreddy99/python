n_friend = ["bakkasai", "keshu","amith","sudheer"]
b_friend = ["prav","bsai","man","harun"]

f_name = raw_input("enter f_nmae: ")

def is_in_names(names,name):
    return name in names

if is_in_names(names=b_friend,name=f_name):
    print "{0} is your best friend".format(f_name)
elif is_in_names(names=n_friend,name=f_name):
    print "{0} is your normal friend".format(f_name)
else:
    print "{0} is not your data base".format(f_name)

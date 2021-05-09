Regex_Pattern = r"^\d{2}\D{1}\d{2}\D{1}\d{4}"	# Do not delete 'r'.

# Note
# It should be "^\d{2}\D{1}\d{2}\D{1}\d{4}$" but test case 4 is broken. The provided pattern in the statement
# is xxXxxXxxxx and the pattern in test case 4 is xxXxxXxxxxxxxxxx.
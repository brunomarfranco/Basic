print("DICTIONARIES")

monthConversions = {
    "Jan": "January",
    2: "February",
    "Mar": "March",
    "Apr": "April",
    5: "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get(2))
print(monthConversions.get("Luv", "Not a valid key"))

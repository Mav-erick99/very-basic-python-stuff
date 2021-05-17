month_conversion={
    "mon":"monday",
    "tue":"tuesday",
    "wed":"wednesday",
    "thur":"thursday",
    "fri":"friday",
    "sat":"saturday",
    "sun":"sunday",
}
print(month_conversion["fri"])
print(month_conversion.get("tue"))
print(month_conversion.get("teu","not a valid key"))
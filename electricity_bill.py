#Augustine
# Assignment Electricity Bill
FIXED_CHARGE = 150
VAT_RATE = 0.16
BAND1_LIMIT = 30
BAND1_RATE = 12
BAND2_LIMIT = 100
BAND2_RATE = 20
BAND3_RATE = 25

home=[
    ("Amina", 1200, 1225),  
    ("Brian", 3400, 3490),
    ("cynthia", 560, 740),
    ("Dan", 900, 880),
    ]
def is_valid_reading(previous, current):
    if current >= previous:
        return True
    else:
        return False

def energy_cost (units):
        if units <= BAND1_LIMIT:
            return units * BAND1_RATE
        elif units <= BAND2_LIMIT:
            return (BAND1_LIMIT * BAND1_RATE) + ((units - BAND1_LIMIT) * BAND2_RATE)
        else:
            return (BAND1_LIMIT * BAND1_RATE) + ((BAND2_LIMIT - BAND1_LIMIT) * BAND2_RATE) + ((units - BAND2_LIMIT) * BAND3_RATE)

def usage_level(units):
     if units <= 50:
        return "low"
     elif units <= 100:
        return "medium"
     else:
         return "high"

def calculate_bill(units, vat_rate=0.16):
    energy = energy_cost(units)
    vat = energy * vat_rate
    total = energy + FIXED_CHARGE + vat
    return energy, (round(vat, 2)), (round(total, 2))

count = 0
total_billed = 0
highest=0
highest_user=""
for name, prev, curr in home:
    if is_valid_reading(prev, curr) == False:
        print(name + ": Invalid reading")
    else:
        units = curr - prev
        level = usage_level(units)
        energy, vat, total = calculate_bill(units)
        print(name + ":", units, "units,", level, ", energy", energy, ", VAT", vat, ", total", total)
        count += 1
        total_billed += total
        if total > highest:
            highest = total
            highest_name = name

print("=bill summary=")
print(count, "bills, total billed", round(total_billed, 2), ", highest bill", highest_name, "with", highest)

print("==Tests==")
print(calculate_bill(90, 0))
print(calculate_bill(30))
print(calculate_bill(100))
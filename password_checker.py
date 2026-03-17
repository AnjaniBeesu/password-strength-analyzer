

password = input("Enter your password: ")

# Check for spaces AFTER input
if " " in password:
    print("Password should not contain spaces ")

length = len(password)

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
has_special = any(char in special_chars for char in password)

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

print("\nPassword Analysis:")
print("Length:", length)
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digits:", has_digit)
print("Special Characters:", has_special)

if score <= 2:
    strength = "Weak "
elif score == 3 or score == 4:
    strength = "Medium "
else:
    strength = "Strong "

print("\nFinal Strength:", strength)

print("\nSuggestions:")

if length < 8:
    print("- Use at least 8 characters")
if not has_upper:
    print("- Add uppercase letters")
if not has_lower:
    print("- Add lowercase letters")
if not has_digit:
    print("- Include numbers")
if not has_special:
    print("- Include special characters like @, #, $")
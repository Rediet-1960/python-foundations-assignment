# Level 2: Count vowels in a string
text = input("Enter a string: ")# Take input from user
vowels = "aeiouAEIOU"# List of vowels
count = 0# Counter to store number of vowels
for char in text:# Loop through each character in the string
    if char in vowels:
        count += 1  # increase count if vowel found
# Print result
print("Number of vowels:", count)
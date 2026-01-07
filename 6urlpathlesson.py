# Language codes include "pt" for Portuguese and "es" for Spanish.
language_code = "es"

# Subjects can be math, science, computing, or humanities.
subject = (input("Enter subject name: "))

url = "https://" + language_code + ".khanacademy.org/" + subject

print("Navigate to the page below!")
print(url)
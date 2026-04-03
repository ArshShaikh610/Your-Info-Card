name = input("What is your name? ")
age = input("What is your age? ")
dream = input("What is your dream? ")

info = {
    "name": name,
    "age": age,
    "dream": dream
}

print("__________________")
print(" Your Info Card")
print("------------------")
print(f"Name: {info["name"]}")
print(f"Age: {info["age"]}")
print(f"Dream: {info["dream"]}")
print("__________________")


print("__________________")
print("  My Reactions")
print("------------------")
print(f"Nice to meet you {name}!")
print(f"Nice! You are {age} years old.")
print(f"So this is your dream? -------> {dream}, nice! I hope you succeed in doing so!")
print("See You Later!!!")
print("__________________")

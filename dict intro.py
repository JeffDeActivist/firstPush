dictionary1 = {1: "ID",
               2: "Age",
               3: "Location",
               4: "First_Dictionary"

               }
# to access dictionary1 values
print(dictionary1[2])
# using .get method to avoid keyError look up
print(dictionary1.get(1))
print(dictionary1.get(10, "does not exist")) # key 10 does not exist
# dict values can also be lists
my_dict = {5: ["ugali", "Chicken", "Vegetables"],
           6: ["beans", "Rice", "Cabbage"]
           }
print(my_dict[5])


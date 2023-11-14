'''class Myclass:
    x = 5
p1 = Myclass()
print(p1.x)'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         def myfunc(self):
#             print("Hello my name is" + self.name)
#             print("Hello my name is" + self.age)
#             p1 = Person(self.name or self.age)
#             print(p1.name)
#             print(p1.age)

import speedtest

def check_internet_speed():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Perform the speed test
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    # Print the results
    print("Download Speed: {:.2f} Mbps".format(download_speed))
    print("Upload Speed: {:.2f} Mbps".format(upload_speed))

# Usage
check_internet_speed()

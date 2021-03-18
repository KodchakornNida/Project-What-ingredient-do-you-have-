# importing required modules
import urllib.request

# setting filename and image URL
filename = 'ยำสตรอว์เบอรี่กุ้งสด.jpg'
image_url = "https://nlovecooking.com/wp-content/uploads/2016/01/food442.jpg"

# calling urlretrieve function to get resource
urllib.request.urlretrieve(image_url, filename)
print(urllib.request.urlretrieve(image_url, filename))
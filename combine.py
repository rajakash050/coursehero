# creating a test input
test = "photoo.jpg,Warsaw,2013-09-05 14:08:15," \
       "tohn.png,London,2015-06-20 15:13:22,2photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "3photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "4photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "5photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "6photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "70photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "8photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "9photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "10photo.jpg,Warsaw,2013-09-05 14:08:15," \
       "john.png,London,2015-06-20 15:13:22,myFriends.png,Warsaw,2013-09-05 14:07:13, Eiffel.jpg, Paris, " \
       "2015-07-23 08:03:02"
# converting the string to a list format
test_list = test.split(",")

temp_dict = {}
result = ""
# iterating over the list of to group on city basis
for i in range(1,len(test_list),3):
    # creating a dict to get the serial number which should be append to the photo name
    if test_list[i] in temp_dict.keys():
        temp_dict[test_list[i].title()].append([test_list[i+1],test_list[i-1]])
    else:
        temp_dict[test_list[i].title()] = [[test_list[i+1],test_list[i-1]]]
    # checking the photo-count available for that city and creating the name accordingly
    # so that if photo count is more than 10 then the name should have "0" before serial number
    if len(temp_dict[test_list[i]]) < 10 and test_list.count(test_list[i]) > 9:
        result += test_list[i].title() + "0" + str(len(temp_dict[test_list[i]])) + "." + test_list[i-1].split(".")[1] + " "
    else:
        # for those whose count is below 10 , "0" should not append to photoname
        result += test_list[i].title() + str(len(temp_dict[test_list[i]])) + "." + test_list[i-1].split(".")[1] + " "

# final output which is expected
print(result)
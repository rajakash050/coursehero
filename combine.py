# Author: Akash
# Script to get proper image names

def get_zeros_to_assign(total_images_of_city, already_processed_count):
    """
    function to get zeros to match serial numbers
    """
    zeros_count = len(str(total_images_of_city)) - len(str(already_processed_count))
    return zeros_count


def get_pics(image_names):
    """
    Function to get process image names to exprected one
    """
    # converting the string to a list format
    image_names_list = image_names.split(",")

    temp_dict = {}
    result = ""
    # iterating over the list of to group on city basis
    for i in range(1, len(image_names_list), 3):
        # creating a dict to get the serial number which should be append to the photo name
        if image_names_list[i] in temp_dict.keys():
            temp_dict[image_names_list[i].title()].append([image_names_list[i+1], image_names_list[i-1]])
        else:
            temp_dict[image_names_list[i].title()] = [[image_names_list[i+1], image_names_list[i-1]]]

        zeros_to_append = get_zeros_to_assign(image_names_list.count(image_names_list[i]), len(temp_dict[image_names_list[i]]))

        # checking the photo-count available for that city and creating the name accordingly
        # so that if photo count is more than 10 then the name should have "0" before serial number

        result += image_names_list[i].title() + "0" * zeros_to_append + str(len(temp_dict[image_names_list[i]])) + "." \
                  + image_names_list[i - 1].split(".")[1] + " "

    return result


if __name__ == '__main__':
    # creating a test input
    random_image_names = "photoo.jpg,Warsaw,2013-09-05 14:08:15," \
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
    
    get_image_names = get_pics(random_image_names)
    
    # final output which is expected
    print(get_image_names)

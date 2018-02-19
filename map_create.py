import folium
from geopy import ArcGIS
from random import randint


def main(user_lst, friends_lst, num):
    map_html = folium.Map()
    geolocator = ArcGIS(timeout=10)
    lst = ["Name: ", "Location: ", "Description: ", "url: ",
           "Followers: ", "Friends: ", "Listed: ", "Created: ",
           "Favourites: ", "Posts: "]

    # Adding User on map

    place = geolocator.geocode(user_lst[1])
    if place == None:
        popup_message = '<img src="{}"/><br>'.format(user_lst[-1])
        for i in range(len(user_lst) - 1):
            popup_message += "{}{}<br>".format(lst[i], user_lst[i])
        map_html.add_child(
            folium.Marker(location=[randint(-90, 90), randint(-180, 180)],
                          popup=popup_message,
                          icon=folium.Icon(color='green')))
    else:
        popup_message = '<img src="{}"/><br>'.format(user_lst[-1])
        for i in range(len(user_lst) - 1):
            popup_message += "{}{}<br>".format(lst[i], user_lst[i])
        map_html.add_child(folium.Marker(location=[place.latitude, place.longitude],
                                         popup=popup_message,
                                         icon=folium.Icon(color='green')))

    # Adding friends on map

    for i in range(len(friends_lst)):
        place = geolocator.geocode(friends_lst[i][1])
        if place == None:
            popup_message = '<img src="{}"/><br>'.format(friends_lst[i][-1])
            for j in range(len(friends_lst[i]) - 1):
                popup_message += "{}{}<br>".format(lst[j], friends_lst[i][j])
            map_html.add_child(
                folium.Marker(location=[randint(-90, 90), randint(-180, 180)],
                              popup=popup_message,
                              icon=folium.Icon(color='red')))
        else:
            popup_message = '<img src="{}"/><br>'.format(friends_lst[i][-1])
            for j in range(len(friends_lst[i]) - 1):
                popup_message += "{}{}<br>".format(lst[j], friends_lst[i][j])
            map_html.add_child(
                folium.Marker(location=[place.latitude, place.longitude],
                              popup=popup_message,
                              icon=folium.Icon(color='red')))


    map_html.save("templates/map_html.html")
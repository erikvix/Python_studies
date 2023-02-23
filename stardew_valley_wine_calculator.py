wine = input("enter wine name: ")
quality = input("enter wine quality: ")

starprice = {
    'normal': 1,
    'silver': 1.25,
    'gold': 1.5,
    'iridium': 3,
}
price = {
    'strawberrry': 240,
    'pinapple': 660,
    'banana': 330,
    'starfruit': 1500,
    'ancient_fruit': 1100,
    'melon': 500,
    'blueberry': 100,
    'cranberry': 150,
    'hot_pepper': 80,
}

print("The {} wine with {} quality is: {}".format(wine, quality ,price[wine] * starprice[quality]))
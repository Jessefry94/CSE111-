import math
#Nice! Job! Yay! #
names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "211", "300", "303"]
radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

def compute_volume(radius, height):
    volume = math.pi * radius**2 *height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency   
    

names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "211", "300", "303"]
radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
#The array below isn't needed for the base assignment, just for the stretch activity.
cost_per_can = [.28, .43, .45, .61, .86, .83, .22, .26, 1.53, .34, .38, .42]

for i in range(len(names)):
        volume = compute_volume(float(radius[i]), float(height[i]))
        surface_area = compute_surface_area(float(radius[i]), float(height[i]))
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
    
        print(f"{names[i]} is {storage_efficiency:.2f} efficient")
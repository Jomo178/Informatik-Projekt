import csv
from turtle import position
from matplotlib.patches import Circle
import matplotlib.pyplot as plt

def plot_street_from_csv(csv_file, save_file):
    # Daten aus der CSV-Datei lesen
    measurements = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Überspringe Header
        for row in reader:
            time, direction, value = int(row[0]), row[1], int(row[2])
            measurements.append((time, direction, value))

    plot_street(measurements, save_file)

def plot_street(measurements, save_file):
    left_lane = []
    right_lane = []

    for measurement in measurements:
        if measurement[1] == 'l':
            left_lane.append(measurement)
        elif measurement[1] == 'r':
            right_lane.append(measurement)

    left_x = [-measurement[2] for measurement in left_lane]
    left_y = [measurement[0] for measurement in left_lane]

    right_x = [measurement[2] for measurement in right_lane]
    right_y = [measurement[0] for measurement in right_lane]
    
    position_car_x = []
    for i in range(len(left_x)):
        position_car_x.append((left_x[i] + right_x[i]) / 2)
    
    # position_car_y = [measurement[0] for measurement in right_lane]
    
    
    
    print(position_car_x)

    plt.plot(left_x, left_y, 'b', label='Left Lane')
    plt.plot(right_x, right_y, 'r', label='Right Lane')
    plt.plot(position_car_x, left_y, 'g', label='Care Position')

    # car_x = 0
    # car_y = (max(left_y) + min(right_y)) / 2
    # circle = Circle((car_x, car_y), 1, color='green', fill=False)
    # plt.gca().add_patch(circle)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('Position')
    plt.ylabel('Time')
    plt.title('Street with Car')
    plt.legend()
    plt.grid(True)

    plt.savefig(save_file)  # Speichern als PNG-Datei
    plt.close()

# CSV-Datei verwenden und Straße zeichnen
csv_file = 'messungen.csv'
save_file = 'street_with_car.png'
plot_street_from_csv(csv_file, save_file)

import csv
import pygame

frc = []
solar_car = []

frc_grid = []
solar_car_grid = []

new_append_frc = []
new_append_slr = []

for i in range(8):
    frc_grid.append([])
    solar_car_grid.append([])




while True:
    with open('logonList.csv',  newline='') as logonList:
        logged_on = csv.reader(logonList)
        with open('users.csv', newline='') as users_csv:
            user_read = csv.reader(users_csv)

            for ir in logged_on:
                for i in ir:
                    print(i)

                    if not((i in solar_car) or (i in frc)):
                        for j in user_read:
                            print(i)
                            print(j[0]+" yoyo")
                            if j[0] == i:
                                print(j)
                                if j[2] == "FRC":
                                    frc.append(i)
                                    print("heyo")
                                    continue
                                elif j[2] == "SLR":
                                    solar_car.append(i)
                                    continue
                                
            if len(new_append_frc) > 0:
                for u in new_append_frc:
                    for k in frc_grid:
                        if len(k) < 5:
                            k.append(u)
                            print(u)
                            continue
                        
            elif len(new_append_slr) > 0:
                for u in new_append_slr:
                    for k in solar_car_grid:
                        if len(k) < 5:
                            k.append(u)
                            print(u)
                            continue






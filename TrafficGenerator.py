import numpy as np
import math
#The **TrafficGenerator** class contain the function dedicated to defining the route of every vehicle in one epsiode. The file created is *tlcs_train.rou.xml* which is placed in the "intersection" folder.
# HANDLE THE GENERATION OF VEHICLES IN ONE EPISODE
class TrafficGenerator:
    def __init__(self, max_steps):
        self._n_cars_generated = 1000  # how many cars per episode
        self._max_steps = max_steps

    # generation of routes of cars
    def generate_routefile(self, seed):
        #np.random.seed(seed)  # make tests reproducible

        # the generation of cars is distributed according to a weibull distribution
        timings = range(self._n_cars_generated)
        #timings = np.sort(timings)

        # reshape the distribution to fit the interval 0:max_steps
        car_gen_steps = []
       # min_old = math.floor(timings[1])
        #max_old = math.ceil(timings[-1])
        #min_new = 0
        #max_new = self._max_steps
        for value in timings:
            car_gen_steps = np.append(car_gen_steps, value)

        car_gen_steps = np.rint(car_gen_steps)  # round every value to int -> effective steps when a car will be generated

        # produce the file for cars generation, one car per line
        with open("intersection/tlcs_train.rou.xml", "w") as routes:
            print("""<routes>
            <vType accel="3.0" vClass="passenger" decel="4.5" id="standard_car" length="5.0" minGap="2.5" maxSpeed="35" sigma="0.5" color="0,0,1" />
            <vType accel="4.5" vClass="emergency" decel="7.5" id="emergency_car" length="7.0" minGap="2.5" maxSpeed="50" sigma="1" color="1,0,1" />
            <vType accel="4.0" vClass="bus" decel="7.5" id="bus" length="10.0" minGap="2.5" maxSpeed="45" sigma="1" color="1,1,1" />
            <vType accel="2.0" vClass="trailer" decel="2.5" id="trailer" length="15.0" minGap="2.5" maxSpeed="30" sigma="0.5" color="0,1,1" />
            
            <route id="W_E" edges="WOUT W2TL TL2E EIN"/>
            
            <route id="W_S_E" edges="WOUT W2S S2E EIN"/>
            <route id="W_N_E" edges="WOUT W2N N2TL TL2E EIN"/>
            
             <route id="W_N" edges="WOUT W2N NIN"/>
            <route id="W_S_N" edges="WOUT W2S S2TL TL2N NIN"/>
            <route id="W_E_N" edges="WOUT W2TL TL2E E2N NIN"/>
            
             <route id="W_S" edges="WOUT W2S SIN"/>
            <route id="W_N_S" edges="WOUT W2N N2TL TL2S SIN"/>
            <route id="W_E_S" edges="WOUT W2TL TL2S SIN"/>
            
            
            <route id="S_N" edges="SOUT S2TL TL2N NIN"/>
            <route id="S_W_N" edges="SOUT S2W W2N NIN"/>
            <route id="S_E_N" edges="SOUT S2E E2TL TL2N NIN"/>
            
             <route id="S_W" edges="SOUT S2W WIN"/>
            <route id="S_N_W" edges="SOUT S2TL TL2N N2W WIN"/>
            <route id="S_E_W" edges="SOUT S2E E2TL TL2W WIN"/>
            
             <route id="S_E" edges="SOUT S2E EIN"/>
            <route id="S_N_E" edges="SOUT S2TL TL2E EIN"/>
            <route id="S_W_E" edges="SOUT S2W W2TL TL2E EIN"/>
            
            
            <route id="E_N" edges="EOUT E2N NIN"/>
            <route id="E_W_N" edges="EOUT E2TL TL2W W2N NIN"/>
            <route id="E_S_N" edges="EOUT E2S S2TL TL2N NIN"/>
            
             <route id="E_W" edges="EOUT E2TL TL2W WIN"/>
            <route id="E_N_W" edges="EOUT E2N N2W WIN"/>
            <route id="E_S_W" edges="EOUT E2S S2TL TL2W WIN"/>
            
             <route id="E_S" edges="EOUT E2S SIN"/>
            <route id="E_N_S" edges="EOUT E2TL TL2S SIN"/>
            <route id="E_W_S" edges="EOUT E2TL TL2W W2S"/>
            
            
            <route id="N_S" edges="NOUT N2TL TL2S SIN"/>
            <route id="N_W_S" edges="NOUT N2W W2S SIN"/>
            <route id="N_E_S" edges="NOUT N2E E2TL TL2S SIN"/>
            
             <route id="N_W" edges="NOUT N2W WIN"/>
            <route id="N_S_W" edges="NOUT N2TL TL2S S2W WIN"/>
            <route id="N_E_W" edges="NOUT N2TL TL2W WIN"/>
            
             <route id="N_E" edges="NOUT N2E EIN"/>
            <route id="N_S_E" edges="NOUT N2TL TL2S S2E EIN"/>
            <route id="N_W_E" edges="NOUT N2W W2TL TL2E EIN"/>
            

            """, file=routes)

            for car_counter, step in enumerate(car_gen_steps):
                straight_or_turn = np.random.uniform()
                if straight_or_turn < 0.6:  # choose direction: straight or turn - 60% of times the car goes straight
                    route_straight = np.random.randint(1, 8)  # choose a random source & destination
                    if route_straight == 1:
                        print('    <vehicle id="veh_%i" type="trailer" route="W_E" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 2:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_W" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 3:
                        print('    <vehicle id="veh_%i" type="bus" route="N_S" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 4:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_N" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 5:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_E" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 6:
                        print('    <vehicle id="veh_%i" type="bus" route="E_W" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_straight == 7:
                        print('    <vehicle id="veh_%i" type="emergency_car" route="N_S" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    else:
                        print('    <vehicle id="veh_%i" type="trailer" route="S_N" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)       

        
                else:  # car that turn -25% of the time the car turns
                    route_turn = np.random.randint(1, 33)  # choose random source source & destination
                    if route_turn == 1:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_N" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 2:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_S" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 3:
                        print('    <vehicle id="veh_%i" type="emergency_car" route="N_W" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 4:
                        print('    <vehicle id="veh_%i" type="standard_car" route="N_E" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 5:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_N" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 6:
                        print('    <vehicle id="veh_%i" type="bus" route="E_S" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 7:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_W" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 8:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_E" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 9:
                        print('    <vehicle id="veh_%i" type="emergency_car" route="W_N_S" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 10:
                        print('    <vehicle id="veh_%i" type="standard_car" route="N_S_W" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 11:
                        print('    <vehicle id="veh_%i" type="bus" route="N_S_E" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 12:
                        print('    <vehicle id="veh_%i" type="standard_car" route="N_W_E" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 13:
                        print('    <vehicle id="veh_%i" type="standard_car" route="N_E_W" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 14:
                        print('    <vehicle id="veh_%i" type="standard_car" route="N_W_S" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 15:
                        print('    <vehicle id="veh_%i" type="trailer" route="N_E_S" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 16:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_W_S" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 17:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_N_W" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 18:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_N_E" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 19:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_E_N" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 20:
                        print('    <vehicle id="veh_%i" type="bus" route="W_E_S" depart="%s" departLane="2" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 21:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_S_W" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 22:
                        print('    <vehicle id="veh_%i" type="standard_car" route="W_S_E" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 23:
                        print('    <vehicle id="veh_%i" type="trailer" route="W_S_N" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 24:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_N_W" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 25:
                        print('    <vehicle id="veh_%i" type="emergency_car" route="S_N_E" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 26:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_E_N" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 27:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_N_S" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 28:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_W_N" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 29:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_E_W" depart="%s" departLane="0" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 30:
                        print('    <vehicle id="veh_%i" type="standard_car" route="S_W_E" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 31:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_W_N" depart="%s" departLane="1" departSpeed="10" />' % (car_counter, step), file=routes)
                    elif route_turn == 32:
                        print('    <vehicle id="veh_%i" type="standard_car" route="E_S_N" depart="%s" departLane="3" departSpeed="10" />' % (car_counter, step), file=routes)

            print("</routes>", file=routes)

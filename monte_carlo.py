import numpy as np
import matplotlib.pyplot as plt

# Functie om de ballen te simuleren
def simulation(amount_photons, square_length, steps):
    # Positie van de oorsprong (midden van het vierkant)
    origin = np.array([0, 0])

    # Creëer een plot
    plt.figure(figsize=(6,6))
    plt.xlim(-square_length/2, square_length/2)
    plt.ylim(-square_length/2, square_length/2)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    
    for i in range(amount_photons):
        # Willekeurige richting (hoek tussen 0 en 2*pi)
        theta = np.random.uniform(0, 2 * np.pi)

        # Bereken de snelheidcomponenten
        dx = np.cos(theta) * steps
        dy = np.sin(theta) * steps

        # Posities van de bal
        position = origin.copy()
        
        # Beweeg de bal totdat deze de rand van het vierkant bereikt
        while np.abs(position[0]) <= square_length / 2 and np.abs(position[1]) <= square_length / 2:
            position += [dx, dy]
            # Als de bal binnen de grenzen van het vierkant is, plot dan de nieuwe positie
            plt.plot(position[0], position[1], 'bo', markersize=1)  

        # Zorg ervoor dat de bal stopt zodra hij de rand heeft bereikt

    plt.gca().set_aspect('equal', adjustable='box')  # Zorg ervoor dat de schaal gelijk is
    plt.show()

# Parameters
amount_photons = 1000  # Aantal ballen
square_length = 10  # Grootte van het vierkant
steps = 0.1  # Hoe ver de bal per stap beweegt

# Run de simulatie
simulation(amount_photons, square_length, steps)
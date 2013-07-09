import os
import sys
import time
import plant_config

plant = plant_config.plant

print plant['start_date']
current_time = time.asctime()



# Check all our sensors, fire off warnings and take any other actions possible.

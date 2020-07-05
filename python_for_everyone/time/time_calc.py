# This function gets the start time string and 
# split it into hours and minutes.
def get_start_times(time):
    current_time, clock = time.split()    
    hour, minutes = current_time.split(':')
    return hour, minutes, clock

# Same thing as above, but for the duration time.
def get_duration_times(time):
    hour, minutes = time.split(':')
    return hour, minutes

# This converts hours into minutes and sums them
# up.
def to_minutes(hour, minutes):
    hour, minutes = int(hour), int(minutes)
    return hour * 60 + minutes

# This converts minutes into hours and and remaining
# into minutes. If there less than 10 minutes, put a 
# zero in front of it.
def to_hours(minutes):
    hours = str(minutes / 60).split(".")[0]
    minutes = minutes % 60

    if minutes < 10:
        minutes = "0" + str(minutes)

    return hours, minutes

# Now this is basically the main function.
def to_am_pm(hours, clock, day):
    hours = int(hours) # Convert the hours string into an integer.
    time_format = {'AM': 'PM', 'PM': 'AM'} #This dict is responsible for converting AM to PM and vice-versa.
    calendar = {
        'sunday'  : 'monday',    'monday'   : 'tuesday', 
        'tuesday' : 'wednesday', 'wednesday': 'thursday',  
        'thursday': 'friday',    'friday'   : 'saturday', 
        'saturday': 'sunday'
    } # Same for time_format variable, but for days of the week.
    days = 0 # How many days have passed since the start.

    previous_turn = clock # Get the time of the day where the counting began.

    while hours >= 12: # Since the time is 12h format, this will loop while there are more than 12 hours.
        clock = time_format[clock] # As there are more than 12 hours, the time format will necessarily be different.
        current_turn = clock # Gets the current format for comparison.

        if previous_turn == 'PM' and current_turn == 'AM': # If the counting started on PM and it changed to AM, then
            days += 1                                      # necessarily a day have passed.
            if day is not None:                            # And, if we were following the days, we should go to the
                day = calendar[day.lower()]                # next one.

        previous_turn = current_turn                       # Now, we update the previous turn into the current one.
        
        if hours > 12:                                     # If there are more than 12 hours, subtract 12 hours.
            hours -= 12            
        else:                                              # Otherwise, break the loop.
            break

    response_string = ''                                   # Then, we define the response string.
    if days == 1:                                          # If a day has elapsed...
        response_string = 'next day'
    elif days > 1:                                         # If more than one day has elapsed...
        response_string = f'{days} days later'             # Otherwise, the response string will be empty.

    return hours, clock, day, response_string

def add_time(start, duration, day=None):
    start_hour, start_minute, clock = get_start_times(start)                # Split the strings.
    duration_hour, duration_minute = get_duration_times(duration)           # Same as above.

    total_time = to_minutes(start_hour, start_minute) + to_minutes(duration_hour, duration_minute)      # Get the total time in minutes.

    total_hours, total_minutes = to_hours(total_time)                                                   # Now, convert it into hours.
    total_hours, time_format, day, response_string = to_am_pm(total_hours, clock, day)                  # Calculate how many days have passed,
                                                                                                        # if any.
    date_string = f'{total_hours}:{total_minutes} {time_format}'                                        # Put it all together.

    if day is not None:
        date_string += f', {day.title()}'
    if len(response_string) > 0:
        date_string += f' ({response_string})'

    return date_string

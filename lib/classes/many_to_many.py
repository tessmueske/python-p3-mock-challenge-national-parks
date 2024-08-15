import re

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name attribute must be a string.")
        if len(value) <= 3:
            raise Exception("Name must be greater than or equal to 3 characters")
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed after instantiated.")
        self._name = value
        
    ####STUDY THIS ONE!######
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
            #full loop:
            # trips_for_park = []
            # for trip in Trip.all:
            #     if trip.national_park == self:
            #         trips_for_park.append(trip)
            # return trips_for_park
    #########################

    ###study this one too
    def visitors(self):
        unique_visitors = []
        for trip in Trip.all: #iterating through Trip.all and not Visitor.all because the trip object holds the info, not the visitor object. Trip is the join table here, not Visitor.
            if trip.national_park == self: 
                if trip.visitor not in unique_visitors:
                    unique_visitors.append(trip.visitor)
        return unique_visitors  
    
    #study this one
    def total_visits(self):
        visit_number = []
        for trip in Trip.all:
            if trip.national_park == self:
                visit_number.append(trip.national_park)
        return len(visit_number)

    
    def best_visitor(self):
        visitor_visit_count = {}
        for trip in self.trips():
            if trip.visitor in visitor_visit_count:
                visitor_visit_count[trip.visitor] += 1
            else:
                visitor_visit_count[trip.visitor] = 1

        if not visitor_visit_count:
            return None

        best_visitor = max(visitor_visit_count, key=visitor_visit_count.get)

        return best_visitor
        
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise Exception("Start date must be a string.")
        if not len(value) >= 7:
            raise Exception("Start date must be greater than or equal to 7 characters.")
        if not re.match(r'^[A-Z][a-z]+\s\d{1,2}(st|nd|rd|th)$', value):
            raise Exception("Start date must be in the format 'Month DaySuffix', e.g., 'September 1st'.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise Exception("End date must be a string.")
        if len(value) < 7:
            raise Exception("End date must be greater than or equal to 7 characters.")
        if not re.match(r'^[A-Z][a-z]+\s\d{1,2}(st|nd|rd|th)$', value):
            raise Exception("End date must be in the format 'Month DaySuffix', e.g., 'September 1st'.")
        self._end_date = value

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if value not in Visitor.all:
            raise Exception("Visitor must be in Visitor list.")
        self._visitor = value
    #     Trip property visitor
    # Returns the Visitor object for that trip
    # Must be of type Visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if value not in NationalPark.all:
            raise Exception("National Park must be in National Park list.")
        self._national_park =  value
        # Trip property national_park
        # Returns the NationalPark object for that trip
        # Must be of type NationalPark

class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name attribute must be a string.")
        if not 1 <= len(value) <= 15:
            raise Exception("Name attribute must be between 1-15 characters")
        self._name = value
        
    def trips(self):
        total_visits = []
        for trip in Trip.all:
            if trip.visitor == self:
                total_visits.append(trip)
        return total_visits
    # Returns a list of all trips for that visitor
    # Trips must be of type Trip
    
    def national_parks(self):
        unique_parks = []
        for trip in Trip.all:
            if trip.visitor == self:  # Check if the trip's visitor is this visitor
                if trip.national_park not in unique_parks:  # Check if the park is already in the list
                    unique_parks.append(trip.national_park)
        #drill into Trip.all to get 
    # Returns a unique list of all parks that visitor has visited
    # Parks must be of type NationalPark
        return unique_parks
    
    def total_visits_at_park(self, park):
        total_visits = []
        if park == self.park:
            total_visits.append(self)
        return len(total_visits)
    # Receives a NationalPark object as argument
    # Returns the total number of times a visitor visited the park passed in as argument
    # Returns 0 if the visitor has never visited the park
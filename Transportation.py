class Transportation(object):
   """Abstract base class"""

   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost( self ):
      """Abstract method; derived classes must override"""
      raise NotImplementedError


class Walk( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      return 0

class Taxi(Transportation):
    def __init__(self, s_p, e_p, rate, d):
        super().__init__(s_p, e_p, d)
        self._rate = rate
        
    def find_cost(self):
        self._cost = super().getD() * self._rate
        return self._cost


   
# main program

travel_cost = 0

#trip = [ Walk("KMITL","KMITL SCB Bank",0.6),
         #Taxi("KMITL SCB Bank","Ladkrabang Station",5),
         #Train("Ladkrabang Station","Payathai Station",40,6),
         #Taxi("Payathai Station","The British Council",3) ]

for travel in trip:
   travel_cost += travel.find_cost()
print(travel_cost)

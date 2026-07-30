class Solution:
    """
     
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse = True) # cars ahead in position help determine final speed of cars behind it

        def timeTaken(car):
            time = (target - car[0]) / car[1]
            return time

        fleets = [timeTaken(cars[0])]
        for car in cars:
            time = timeTaken(car)
            if fleets[-1] < time:
                fleets.append(time)

        return len(fleets)

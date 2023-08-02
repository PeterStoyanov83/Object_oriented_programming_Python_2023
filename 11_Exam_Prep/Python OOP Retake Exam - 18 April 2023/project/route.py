class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        if not start_point.strip():
            raise ValueError("Start point cannot be empty!")
        if not end_point.strip():
            raise ValueError("End point cannot be empty!")
        if length < 1.00:
            raise ValueError("Length cannot be less than 1.00 kilometer!")

        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

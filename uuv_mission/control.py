class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute_action(self, reference: float, measurement: float) -> float:
        error = reference - measurement
        action = self.kp * error + self.kd * (error - self.previous_error)
        self.previous_error = error
        return action

    def reset(self):
        self.previous_error = 0.0

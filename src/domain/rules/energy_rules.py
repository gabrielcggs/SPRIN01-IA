class EnergyRules:

    @staticmethod
    def overload_detected(current_usage, max_capacity):

        return current_usage > max_capacity

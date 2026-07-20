import math

class SwivelRakeSimulation:
    def __init__(self, arm_length_m=1.2, joint_yield_strength_mpa=250):
        self.arm_length = arm_length_m  # meters
        self.yield_strength = joint_yield_strength_mpa * 1e6  # Pascals

    def calculate_swivel_stress(self, applied_force_n, angle_degrees):
        """Calculates torque and stress on the swivel joint mechanism."""
        angle_rad = math.radians(angle_degrees)
        torque = applied_force_n * self.arm_length * math.sin(angle_rad)
        
        # Approximate shear stress on swivel pin (assuming 15mm steel pin)
        pin_radius = 0.0075  # 7.5 mm
        pin_area = math.pi * (pin_radius ** 2)
        shear_stress = applied_force_n / pin_area
        
        safety_factor = self.yield_strength / max(shear_stress, 1)
        
        return {
            "torque_nm": round(torque, 2),
            "shear_stress_mpa": round(shear_stress / 1e6, 2),
            "safety_factor": round(safety_factor, 2),
            "status": "PASS" if safety_factor > 1.5 else "WARNING: High Stress"
        }

if __name__ == "__main__":
    sim = SwivelRakeSimulation()
    # Simulate 150 N force applied at a 45-degree angle
    result = sim.calculate_swivel_stress(applied_force_n=150, angle_degrees=45)
    print("Swivel Rake Simulation Results:", result)

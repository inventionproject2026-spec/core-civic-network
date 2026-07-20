Python
import math

class WeedTrimmerSimulation:
    def __init__(self, rpm=8000, trimmer_head_radius_m=0.15, reservoir_capacity_l=1.0):
        self.rpm = rpm  # Revolutions per minute
        self.head_radius = trimmer_head_radius_m  # meters
        self.reservoir_capacity = reservoir_capacity_l  # liters
        self.fluid_density_kg_l = 1.0  # approximate density for liquid (water/solution)

    def calculate_cutting_kinetics(self, line_mass_grams=5.0):
        """Calculates line tip speed and centrifugal force on the cutting head."""
        line_mass_kg = line_mass_grams / 1000.0
        angular_velocity = (2 * math.pi * self.rpm) / 60.0  # rad/s
        
        tip_speed_mps = angular_velocity * self.head_radius
        tip_speed_mph = tip_speed_mps * 2.23694
        
        # Centrifugal force F = m * omega^2 * r
        centrifugal_force_n = line_mass_kg * (angular_velocity ** 2) * self.head_radius
        
        return {
            "tip_speed_mps": round(tip_speed_mps, 2),
            "tip_speed_mph": round(tip_speed_mph, 2),
            "centrifugal_force_n": round(centrifugal_force_n, 2)
        }

    def calculate_payload_impact(self, current_liquid_level_l):
        """Calculates total head weight and added dynamic load from the reservoir payload."""
        fluid_mass_kg = current_liquid_level_l * self.fluid_density_kg_l
        base_head_mass_kg = 1.2  # Base mechanical housing weight
        
        total_active_mass_kg = base_head_mass_kg + fluid_mass_kg
        added_weight_percentage = ((fluid_mass_kg) / base_head_mass_kg) * 100
        
        return {
            "fluid_mass_kg": round(fluid_mass_kg, 2),
            "total_head_mass_kg": round(total_active_mass_kg, 2),
            "added_weight_percent": round(added_weight_percentage, 1)
        }

if __name__ == "__main__":
    trimmer = WeedTrimmerSimulation(rpm=8500, reservoir_capacity_l=1.2)
    
    print("--- Cutting Performance ---")
    kinetics = trimmer.calculate_cutting_kinetics(line_mass_grams=6.0)
    print(f"Tip Speed: {kinetics['tip_speed_mph']} mph ({kinetics['tip_speed_mps']} m/s)")
    print(f"Centrifugal Force: {kinetics['centrifugal_force_n']} N")
    
    print("\n--- Liquid Payload Analysis (Full Reservoir) ---")
    payload = trimmer.calculate_payload_impact(current_liquid_level_l=1.2)
    print(f"Total Head Mass: {payload['total_head_mass_kg']} kg")
    print(f"Added Mass from Liquid: +{payload['added_weight_percent']}%")

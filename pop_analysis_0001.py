# Population Projection Model: Kenya (2026-2037)
from dataclasses import dataclass, asdict
import math, json

@dataclass
class PopulationModel:
    region: str
    base_pop: int
    area_km2: float
    growth_pct: float
    urban_pct: float

    def project(self, years: int) -> int:
        return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

    def urban_pop(self, years: int) -> int:
        return int(round(self.project(years) * (self.urban_pct / 100.0)))

    def density(self, years: int) -> float:
        return round(self.project(years) / self.area_km2, 2)

    def doubling_years(self) -> float:
        return round(math.log(2.0) / math.log(1.0 + self.growth_pct / 100.0), 2)

def simulate_0001() -> dict:
    m = PopulationModel('Kenya', 56400000, 580367, 3.11, 29.5)
    total = m.project(11)
    return {'region': m.region, 'year': 2037, 'pop': total, 'urban': m.urban_pop(11), 'density': m.density(11), 'doubling': m.doubling_years(), 'meta': asdict(m)}

if __name__ == '__main__':
    print(json.dumps(simulate_0001(), indent=2))
        


# Population Projection Model: Tanzania (2026-2038)
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

def simulate_0002() -> dict:
    m = PopulationModel('Tanzania', 68500000, 945087, 2.33, 37.4)
    total = m.project(12)
    return {'region': m.region, 'year': 2038, 'pop': total, 'urban': m.urban_pop(12), 'density': m.density(12), 'doubling': m.doubling_years(), 'meta': asdict(m)}

if __name__ == '__main__':
    print(json.dumps(simulate_0002(), indent=2))
        
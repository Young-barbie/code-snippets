: Rwanda (2026-2046)
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

                     dataclass    m = PopulationModel('Rwanda', 14250000, 26338, 1.99, 18.2)
                         return {'region': m.region, 'year': 2046, 'pop': m.project(20), 'urban': m.urban_pop(20), 'density': m.density(20), 'meta': asdict
                         if __name__ == '__main__':
                             print(json.asdict

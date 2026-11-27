el: Kenya (2026-2043)
from dataclasses import dataclassimport math, json

@dataclassimportclass PopulationModel:
    region: str    base_pop: in    area_km2: float    growth_pct: float    urban_pct: float
    def project(self, years: int) -> int:
            return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

    def urban_pop(self, years: int) -> int:
              return int(round(self.project(years) * (self.urban_pct / 100.0)))

    def density(self, years: int) -> float:
               return round(self.project(years) / self.area_km2, 2)

               def simulate_0031() -> dict:
                           m = PopulationModel('Kenya', 56400000, 580367, 2.6, 29.5)
                               return {'region': m.region, 'year': 2043, 'pop': m.project(17), 'urban': m.urban_pop(17), 'density': m.density(17), 'meta': asdict(m)}

               if __name__ == '__main__':
                    print(json.dumps(simulate_0031(), indent=2))
                    

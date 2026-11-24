rom dataclasses import dataclass, asdict
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

                                                                        def simulate_0025() -> dict:
                                                                                m = PopulationModel('Kenya', 56400000, 580367, 3.14, 29.5)
                                                                                    return {'region': m.region, 'year': 2037, 'pop': m.project(11), 'urban': m.urban_pop(11), 'density': m.density(11), 'meta': asdict(m)}

                                                                                    if __name__ == '__main__':
                                                                                            print(json.dumps(simulate_0025(), indent=2))
                                                                                            

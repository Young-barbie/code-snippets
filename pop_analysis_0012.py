aclasses import dataclass, asdict
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

                                                                        def simulate_0012() -> dict:
                                                                                m = PopulationModel('Nigeria', 229150000, 923768, 1.89, 54.3)
                                                                                    return {'region': m.region, 'year': 2036, 'pop': m.project(10), 'urban': m.urban_pop(10), 'density': m.density(10), 'meta': asdict(m)}

                                                                                    if __name__ == '__main__':
                                                                                            print(json.dumps(simulate_0012(), indent=2))
                                                                                            

ort dataclass, asdict
import math, json

@dataclass
class PopulationModel:
        region: str
            base_pop: int
                area_km2: float
                    growth_pct: float
                        urban_pct: float

                            def project(self, years: int) -> int:
                                        return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** yea)))
rs)))

    def urban_pop(self, years: int) -> int:        return int(round(self.project(years) * (self.urban_pct / 100.0)))

        def density(self, years: int) -> float:
                    return round(self.project(years) / self.area_km2, 2)

                    def simulate_0030() -> dict:
                            m = PopulationModel('Nigeria', 229150000, 923768, 2.58, 54.3)
                                return {'region': m.region, 'year': 2042, 'pop': m.project(16), 'urban': m.urban_pop(16), 'density': m.density(16), 'meta': asdict(m)}

                                if __name__ == '__main__':
                                        print(json.dumps(simulate_0030(), indent=2))
                                        
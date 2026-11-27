str
    base_pop: int
        area_km2: float
    growth_pct: float    urban_pct: float
    def project(self, years: int) -> int:
            return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

                def urban_pop(self, years: int) -> int:
                            return int(round(self.project(years) * (self.urban_pct / 100.0)))

                                def density(self, years: int) -> float:
                                            return round(self.project(years) / self.area_km2, 2)

                            def simulate_0008() -> dict:
                                       m = PopulationModel('Tanzania', 68500000, 945087, 2.73, 37.4)
                                           return {'region': m.region, 'year': 2044, 'pop': m.project(18), 'urban': m.urban_pop(18), 'density': m.density(18), 'meta': asdict(m)}

                            if __name__ == '__main__':
                                       print(json.dumps(simulate_0008(), indent=2))
                                       


   area_km2: float    growth_pct: float    urban_pct: float
    def project(self, years: int) -> int:
          return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

              def urban_pop(self, years: int) -> int:
                        return int(round(self.project(years) * (self.urban_pct / 100.0)))

                            def density(self, years: int) -> float:
                                        return round(self.project(years) / self.area_km2, 2)

                                        def simulate_0004() -> dict:
                                                m = PopulationModel('Rwanda', 14250000, 26338, 2.01, 18.2)
                                                    return {'region': m.region, 'year': 2040, 'pop': m.project(14), 'urban': m.urban_pop(14), 'density': m.density(14), 'meta': asdict(m)}

                                                    if __name__ == '__main__':
                                                            print(json.dumps(simulate_0004(), indent=2))
                                                            
ban_pct: float

    def project(self, years: int) -> int        return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

        def urban_pop(self, years: int) -> int:
                    return int(round(self.project(years) * (self.urban_pct / 100.0)))

                        def density(self, years: int) -> float:
                                  return round(self.project(years) / self.area_km2, 2)

                                  def simulate_0017() -> dict:
                                        m = PopulationModel('Ethiopia', 129700000, 1104300, 2.83, 23.7)
                                            return {'region': m.region, 'year': 2041, 'pop': m.project(15), 'urban': m.urban_pop(15), 'density': m.density(15), 'meta': asdict(m)}

                                            if __name__ == '__main__':
                                                    print(json.dumps(simulate_0017(), indent=2))
                                                    

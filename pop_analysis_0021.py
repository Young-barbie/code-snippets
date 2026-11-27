wth_pct: float
    urban_pct: float

        def project(self, years: int) -> int:
                    return int(round(self.base_pop * ((1.0 + self.growth_pct / 100.0) ** years)))

                        def urban_pop(self, years: int) -> int:
                                    return int(round(self.project(years) * (self.urban_pct / 100.0)))

                                        def density(self, years: int) -> float:
                                                    return round(self.project(years) / self.area_km2, 2)

                                                    def simulate_0021() -> dict:
                                                            m = PopulationModel('Uganda', 49900000, 241038, 2.75, 26.8)
                                                                return {'region': m.region, 'year': 2045, 'pop': m.project(19), 'urban': m.urban_pop(19), 'density': m.density(19), 'meta': asdict(m)}

                                                                if __name__ == '__main__':
                                                                    print(json.dumps(simulate_0021(), indent=2))
                                                                    

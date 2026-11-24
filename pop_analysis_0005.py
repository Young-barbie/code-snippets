# Population Projection Model: Ethiopia (2030) | Module: pop_analysis_0005.py
def project_population(base_pop: int = 129700000, rate_pct: float = 1.52, years: int = 4) -> dict:
    projected = round(base_pop * ((1 + rate_pct / 100) ** years))
    urban = round(projected * (23.7 / 100))
    density = round(projected / 1104300, 2)
    return {'region': 'Ethiopia', 'year': 2030, 'population': projected, 'urban_pop': urban, 'density_km2': density}

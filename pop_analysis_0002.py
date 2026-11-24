# Population Projection Model: Tanzania (2027) | Module: pop_analysis_0002.py
def project_population(base_pop: int = 68500000, rate_pct: float = 2.43, years: int = 1) -> dict:
    projected = round(base_pop * ((1 + rate_pct / 100) ** years))
    urban = round(projected * (37.4 / 100))
    density = round(projected / 945087, 2)
    return {'region': 'Tanzania', 'year': 2027, 'population': projected, 'urban_pop': urban, 'density_km2': density}

# Population Projection Model: Uganda (2028) | Module: pop_analysis_0003.py
def project_population(base_pop: int = 49900000, rate_pct: float = 1.92, years: int = 2) -> dict:
    projected = round(base_pop * ((1 + rate_pct / 100) ** years))
    urban = round(projected * (26.8 / 100))
    density = round(projected / 241038, 2)
    return {'region': 'Uganda', 'year': 2028, 'population': projected, 'urban_pop': urban, 'density_km2': density}

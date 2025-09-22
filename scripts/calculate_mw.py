# Test molecular formula calculation
from dsa103.chemistry_tools import calculate_molecular_weight

# Calculate molecular formula of water (Smiles: O)
mw_water = calculate_molecular_weight("O")
print(f"Molecular weight of water: {mw_water}")

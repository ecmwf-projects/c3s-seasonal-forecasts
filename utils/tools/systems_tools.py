"""
Utility functions for working with forecast system configurations.
"""

import yaml
from pathlib import Path


def getForecastsystemDetails(strfcsystem):
    """
    Retrieve details for a forecast system based on its identifier.
    
    Parameters:
    -----------
    strfcsystem : str
        Forecast system identifier in the format "{origin}.s{system}"
        Example: "meteo_france.s9" or "ecmwf.s5"
    
    Returns:
    --------
    dict
        A dictionary containing all relevant details for the forecast system,
        including information from both origins.yml and systems.yml.
        The structure includes origin information, system name, and system-specific details.
    
    Raises:
    -------
    ValueError
        If the input format is invalid or if the system is not found in configuration.
    """
    
    # Parse the input string
    try:
        origin_part, system_part = strfcsystem.split('.')
        if not system_part.startswith('s'):
            raise ValueError(f"Invalid system format: {strfcsystem}. Expected format: '{{origin}}.s{{system_number}}'")
        system_num = int(system_part[1:])
    except (ValueError, IndexError) as e:
        raise ValueError(f"Invalid forecast system format: {strfcsystem}. Expected format: 'origin.s#' (e.g., 'meteo_france.s9')") from e
    
    # Get the config directory path
    config_dir = Path(__file__).parent.parent / 'configs'
    
    # Load origins configuration
    origins_file = config_dir / 'origins.yml'
    with open(origins_file, 'r') as f:
        origins_config = yaml.safe_load(f)
    
    # Load systems configuration
    systems_file = config_dir / 'systems.yml'
    with open(systems_file, 'r') as f:
        systems_config = yaml.safe_load(f)
    
    # Validate origin exists
    if origin_part not in origins_config:
        available_origins = list(origins_config.keys())
        raise ValueError(f"Origin '{origin_part}' not found. Available origins: {available_origins}")
    
    # Validate system exists for the origin
    if origin_part not in systems_config or system_num not in systems_config[origin_part]:
        if origin_part in systems_config:
            available_systems = list(systems_config[origin_part].keys())
            raise ValueError(f"System 's{system_num}' not found for origin '{origin_part}'. Available systems: {available_systems}")
        else:
            raise ValueError(f"No systems found for origin '{origin_part}'")
    
    # Build the result dictionary
    result = {
        # 'forecast_system_id': strfcsystem,
        # 'origin': origin_part,
        # 'system_number': system_num,
        'origin_details': origins_config[origin_part].copy(),
        'system_details': systems_config[origin_part][system_num].copy()
    }
    
    return result

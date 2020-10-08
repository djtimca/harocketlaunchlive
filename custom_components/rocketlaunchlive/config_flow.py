"""Config flow for Rocket Launch Live - Next 5 Launches."""
from rocketlaunchlive import RocketLaunchLive

from homeassistant import config_entries
from homeassistant.helpers import config_entry_flow

from .const import DOMAIN


async def _async_has_devices(hass) -> bool:
    """Return if there are devices that can be discovered."""
    api_client = RocketLaunchLive()

    devices = await api_client.get_next_launches()
    return len(devices["result"]) > 0


config_entry_flow.register_discovery_flow(
    DOMAIN,
    "Rocket Launch Live - Next 5 Launches",
    _async_has_devices,
    config_entries.CONN_CLASS_UNKNOWN,
)

import logging

from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http.view import HomeAssistantView
from homeassistant.components.http import StaticPathConfig

import json
from os import walk, path

LOGGER = logging.getLogger(__name__)

DOMAIN = "cupertino"

DATA_EXTRA_MODULE_URL = 'frontend_extra_module_url'
LOADER_URL = f'/{DOMAIN}/main.js'
LOADER_PATH = f'custom_components/{DOMAIN}/main.js'
ICONS_URL = f'/{DOMAIN}/icons'
ICONLIST_URL = f'/{DOMAIN}/list'
ICONS_PATH = f'custom_components/{DOMAIN}/data'


class ListingView(HomeAssistantView):
    requires_auth = False

    def __init__(self, url, iconpath):
        self.url = url
        self.iconpath = iconpath
        self.name = "Icon Listing"

    async def get(self, request):
        """Handle GET request asynchronously."""
        hass = request.app["hass"]  # Get Home Assistant instance
        LOGGER.debug("Icon listing requested at %s", self.url)
        
        # Run os.walk() in a separate thread
        icons = await hass.async_add_executor_job(self._scan_icons)

        LOGGER.debug("Icons found: %s", icons)
        return self.json(icons)

    def _scan_icons(self):
        """Scan the icon directory synchronously but offload it from the event loop."""
        icons = []
        for (dirpath, _, filenames) in walk(self.iconpath):
            icons.extend([
                {"name": path.join(dirpath[len(self.iconpath):], fn[:-4])}
                for fn in filenames if fn.endswith(".svg")
            ])
        return icons

async def async_setup(hass, config):
    # Register the JavaScript loader asynchronously
    await hass.http.async_register_static_paths([
        StaticPathConfig(LOADER_URL, hass.config.path(LOADER_PATH), True)
    ])

    # Register extra module URL
    hass.data.setdefault(DATA_EXTRA_MODULE_URL, set()).add(LOADER_URL)

    # Register the icons path asynchronously
    await hass.http.async_register_static_paths([
        StaticPathConfig(
            ICONS_URL + "/ios", 
            hass.config.path(ICONS_PATH + "/ios"), 
            True
        )
    ])

    # Register the view for icons
    hass.http.register_view(
        ListingView(
            ICONLIST_URL + "/ios",
            hass.config.path(ICONS_PATH + "/ios")
        )
    )

    return True


async def async_setup_entry(hass, entry):
    return True


async def async_remove_entry(hass, entry):
    return True
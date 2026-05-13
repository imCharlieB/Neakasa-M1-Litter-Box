from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
import voluptuous as vol

DOMAIN = "neakasa_m1"

class NeakasaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Here you would validate credentials with the API
            # For now, just accept and create the entry
            return self.async_create_entry(title=user_input[CONF_USERNAME], data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_USERNAME): str,
            vol.Required(CONF_PASSWORD): str,
        })
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)

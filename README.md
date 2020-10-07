# Home Assistant Custom Component for Rocket Launch Live - Next 5 Global Launches

<a target="_blank" href="https://www.buymeacoffee.com/djtimca"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy me a coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;"></a> [![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

The status of the next 5 launches will be returned as five individual sensors with additional data shared in the attributes:

## Usage

### Install through HACS:

Add a custom repository in HACS pointed to https://github.com/djtimca/harocketlaunchlive

The new integration for Rocket Launch Live should appear under your integrations tab.

Click Install and restart Home Assistant.

### Install manually:

Copy the contents found in https://github.com/djtimca/harocketlaunchlive/custom_components/rocketlaunchlive to your custom_components folder in Home Assistant.

Restart Home Assistant.

### Activate the sensors:

Go to Configuration -> Integrations and click the + to add a new integration.

Search for Rocket Launch Live and you will see the integration available.

Click add, confirm you want to install, and voila... you have the status of the next 5 launches as sensors in your Home Assistant.

Enjoy!

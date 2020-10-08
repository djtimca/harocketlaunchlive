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

### Display the data using the custom:button-card

You can easily display the data using the custom:button-card lovelace template from HACS:

<img src="https://github.com/djtimca/harocketlaunchlive/images/lovelace.png">

```
type: vertical-stack
title: Next 5 Rocket Launches
cards:
  - type: 'custom:button-card'
    entity: sensor.rocket_launch_1
    show_name: false
    show_state: true
    show_icon: false
    layout: icon_state
    styles:
      card:
        - font-size: 12px
        - padding: 10px
      grid:
        - grid-template-areas: >-
            "s" "provider" "vehicle" "launch_pad" "location" "target_date"
            "tags"
        - grid-template-columns: 1fr
        - grid-template-rows: 1fr min-content min-content min-content
      state:
        - font-weight: bold
        - font-size: 16px
        - align-self: start
        - justify-self: start
      custom_fields:
        provider:
          - align-self: start
          - justify-self: start
        vehicle:
          - align-self: start
          - justify-self: start
        launch_pad:
          - align-self: start
          - justify-self: start
        location:
          - align-self: start
          - justify-self: start
        target_date:
          - align-self: start
          - justify-self: start
        tags:
          - align-self: start
          - justify-self: start
    custom_fields:
      provider: |
        [[[
          return `Provider: ${states['sensor.rocket_launch_1'].attributes["provider"]}`
        ]]]
      vehicle: |
        [[[
          return `Vehicle: ${states['sensor.rocket_launch_1'].attributes['vehicle']}`
        ]]]
      launch_pad: |
        [[[
          return `Launch Pad: ${states['sensor.rocket_launch_1'].attributes['launch_pad']}`
        ]]]
      location: |
        [[[
          return `Location: ${states['sensor.rocket_launch_1'].attributes['launch_location']}`
        ]]]
      target_date: |
        [[[
          return `Target Date: ${states['sensor.rocket_launch_1'].attributes['launch_date_target']}`
        ]]]
      tags: |
        [[[
          return `Tags: ${states['sensor.rocket_launch_1'].attributes['tags']}`
        ]]]
  - type: 'custom:button-card'
    entity: sensor.rocket_launch_2
    show_name: false
    show_state: true
    show_icon: false
    layout: icon_state
    styles:
      card:
        - font-size: 12px
        - padding: 10px
      grid:
        - grid-template-areas: >-
            "s" "provider" "vehicle" "launch_pad" "location" "target_date"
            "tags"
        - grid-template-columns: 1fr
        - grid-template-rows: 1fr min-content min-content min-content
      state:
        - font-weight: bold
        - font-size: 16px
        - align-self: start
        - justify-self: start
      custom_fields:
        provider:
          - align-self: start
          - justify-self: start
        vehicle:
          - align-self: start
          - justify-self: start
        launch_pad:
          - align-self: start
          - justify-self: start
        location:
          - align-self: start
          - justify-self: start
        target_date:
          - align-self: start
          - justify-self: start
        tags:
          - align-self: start
          - justify-self: start
    custom_fields:
      provider: |
        [[[
          return `Provider: ${states['sensor.rocket_launch_2'].attributes["provider"]}`
        ]]]
      vehicle: |
        [[[
          return `Vehicle: ${states['sensor.rocket_launch_2'].attributes['vehicle']}`
        ]]]
      launch_pad: |
        [[[
          return `Launch Pad: ${states['sensor.rocket_launch_2'].attributes['launch_pad']}`
        ]]]
      location: |
        [[[
          return `Location: ${states['sensor.rocket_launch_2'].attributes['launch_location']}`
        ]]]
      target_date: |
        [[[
          return `Target Date: ${states['sensor.rocket_launch_2'].attributes['launch_date_target']}`
        ]]]
      tags: |
        [[[
          return `Tags: ${states['sensor.rocket_launch_2'].attributes['tags']}`
        ]]]
  - type: 'custom:button-card'
    entity: sensor.rocket_launch_3
    show_name: false
    show_state: true
    show_icon: false
    layout: icon_state
    styles:
      card:
        - font-size: 12px
        - padding: 10px
      grid:
        - grid-template-areas: >-
            "s" "provider" "vehicle" "launch_pad" "location" "target_date"
            "tags"
        - grid-template-columns: 1fr
        - grid-template-rows: 1fr min-content min-content min-content
      state:
        - font-weight: bold
        - font-size: 16px
        - align-self: start
        - justify-self: start
      custom_fields:
        provider:
          - align-self: start
          - justify-self: start
        vehicle:
          - align-self: start
          - justify-self: start
        launch_pad:
          - align-self: start
          - justify-self: start
        location:
          - align-self: start
          - justify-self: start
        target_date:
          - align-self: start
          - justify-self: start
        tags:
          - align-self: start
          - justify-self: start
    custom_fields:
      provider: |
        [[[
          return `Provider: ${states['sensor.rocket_launch_3'].attributes["provider"]}`
        ]]]
      vehicle: |
        [[[
          return `Vehicle: ${states['sensor.rocket_launch_3'].attributes['vehicle']}`
        ]]]
      launch_pad: |
        [[[
          return `Launch Pad: ${states['sensor.rocket_launch_3'].attributes['launch_pad']}`
        ]]]
      location: |
        [[[
          return `Location: ${states['sensor.rocket_launch_3'].attributes['launch_location']}`
        ]]]
      target_date: |
        [[[
          return `Target Date: ${states['sensor.rocket_launch_3'].attributes['launch_date_target']}`
        ]]]
      tags: |
        [[[
          return `Tags: ${states['sensor.rocket_launch_3'].attributes['tags']}`
        ]]]
  - type: 'custom:button-card'
    entity: sensor.rocket_launch_4
    show_name: false
    show_state: true
    show_icon: false
    layout: icon_state
    styles:
      card:
        - font-size: 12px
        - padding: 10px
      grid:
        - grid-template-areas: >-
            "s" "provider" "vehicle" "launch_pad" "location" "target_date"
            "tags"
        - grid-template-columns: 1fr
        - grid-template-rows: 1fr min-content min-content min-content
      state:
        - font-weight: bold
        - font-size: 16px
        - align-self: start
        - justify-self: start
      custom_fields:
        provider:
          - align-self: start
          - justify-self: start
        vehicle:
          - align-self: start
          - justify-self: start
        launch_pad:
          - align-self: start
          - justify-self: start
        location:
          - align-self: start
          - justify-self: start
        target_date:
          - align-self: start
          - justify-self: start
        tags:
          - align-self: start
          - justify-self: start
    custom_fields:
      provider: |
        [[[
          return `Provider: ${states['sensor.rocket_launch_4'].attributes["provider"]}`
        ]]]
      vehicle: |
        [[[
          return `Vehicle: ${states['sensor.rocket_launch_4'].attributes['vehicle']}`
        ]]]
      launch_pad: |
        [[[
          return `Launch Pad: ${states['sensor.rocket_launch_4'].attributes['launch_pad']}`
        ]]]
      location: |
        [[[
          return `Location: ${states['sensor.rocket_launch_4'].attributes['launch_location']}`
        ]]]
      target_date: |
        [[[
          return `Target Date: ${states['sensor.rocket_launch_4'].attributes['launch_date_target']}`
        ]]]
      tags: |
        [[[
          return `Tags: ${states['sensor.rocket_launch_4'].attributes['tags']}`
        ]]]
  - type: 'custom:button-card'
    entity: sensor.rocket_launch_5
    show_name: false
    show_state: true
    show_icon: false
    layout: icon_state
    styles:
      card:
        - font-size: 12px
        - padding: 10px
      grid:
        - grid-template-areas: >-
            "s" "provider" "vehicle" "launch_pad" "location" "target_date"
            "tags"
        - grid-template-columns: 1fr
        - grid-template-rows: 1fr min-content min-content min-content
      state:
        - font-weight: bold
        - font-size: 16px
        - align-self: start
        - justify-self: start
      custom_fields:
        provider:
          - align-self: start
          - justify-self: start
        vehicle:
          - align-self: start
          - justify-self: start
        launch_pad:
          - align-self: start
          - justify-self: start
        location:
          - align-self: start
          - justify-self: start
        target_date:
          - align-self: start
          - justify-self: start
        tags:
          - align-self: start
          - justify-self: start
    custom_fields:
      provider: |
        [[[
          return `Provider: ${states['sensor.rocket_launch_5'].attributes["provider"]}`
        ]]]
      vehicle: |
        [[[
          return `Vehicle: ${states['sensor.rocket_launch_5'].attributes['vehicle']}`
        ]]]
      launch_pad: |
        [[[
          return `Launch Pad: ${states['sensor.rocket_launch_5'].attributes['launch_pad']}`
        ]]]
      location: |
        [[[
          return `Location: ${states['sensor.rocket_launch_5'].attributes['launch_location']}`
        ]]]
      target_date: |
        [[[
          return `Target Date: ${states['sensor.rocket_launch_5'].attributes['launch_date_target']}`
        ]]]
      tags: |
        [[[
          return `Tags: ${states['sensor.rocket_launch_5'].attributes['tags']}`
        ]]]
```

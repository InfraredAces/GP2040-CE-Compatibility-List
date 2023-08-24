# Getting Started

## Overview

This repo utilises Github Actions to generate a README by copying TEMPLATE and replacing the placeholder text with Markdown tables generated from the CSVs using a python script. Once the new README is generated, this action then pushes the changes from main to the publish branch where the Github page-deployment-build action runs and generates the static site.

## Updating README.md

In order to update the README, the TEMPLATE must be updated as this will then be copied by the python script when merged into main.

## CSV Format

### GP2040-CE Compatibility List - PS5 Games.csv

Timestamp,Game Title,GP2040-CE,Notes,"Name, Discord Username, or Gamer Tag"

### GP2040-CE Compatibility List - USB Passthrough.csv

Timestamp	Manufacturer,Controller-Dongle,Console Compatibility,Notes,Link,"Name, Discord Username, or Gamer Tag"

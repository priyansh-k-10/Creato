# Creato Core

Creato Core is the base module for the Creato project.
It provides shared assets, base configuration, and common logic
used by other Creato modules.

## Module Information

- **Technical name**: creato_core
- **Category**: Tools
- **Depends on**: base
- **Application**: Yes

## Features

- Base module structure for Creato
- Static assets (CSS / JS)
- Test scaffolding
- Ready for extension by other modules

## Directory Structure

- `static/` – CSS, JavaScript, and image assets
- `tests/` – Automated tests for module validation
- `views/` – XML views (menus, actions, templates)
- `security/` – Access control rules
- `data/` – Initial data and configuration

## Installation

1. Place the module inside an Odoo addons path
2. Restart the Odoo server
3. Update the Apps list
4. Install **Creato Core** from Apps

## Development Notes

- This module currently contains no business models
- It is intended to be extended by dependent modules
- Safe to install on all databases

## Author

Priyansh Khatri

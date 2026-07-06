## [unreleased]

### 🚀 Features

- Beta add duplicate song player
- Player for duplicates
- Add album search and detail view
- Search for barcode in navigation
- Add description to each page
- Reduce plotly size by using plotly partial cartesian 3.6.0
- Allow sorting albums by completeness
- Add a player for duplicates

### 🐛 Bug Fixes

- *(deps)* Update dependency pydantic-settings to v2.13.0
- *(deps)* Update dependency fastapi to v0.129.0
- *(deps)* Update dependency fastapi to v0.131.0
- *(deps)* Update dependency pydantic-settings to v2.13.1
- *(deps)* Update dependency fastapi to v0.132.0
- *(deps)* Update dependency fastapi to v0.133.1
- *(deps)* Update dependency fastapi to v0.135.1
- *(deps)* Update dependency logfmter to v0.0.12
- *(deps)* Update dependency fastapi to v0.135.2
- *(deps)* Update dependency fastapi to v0.135.3
- Typing errors reported by ty
- *(deps)* Update dependency pydantic to v2.13.0
- *(deps)* Update dependency pydantic to v2.13.1
- *(deps)* Update dependency fastapi to v0.136.0
- *(deps)* Update dependency pydantic to v2.13.2
- Catch exception if config file cannot be found
- *(deps)* Update dependency pydantic-settings to v2.14.0
- *(deps)* Update dependency pydantic to v2.13.3
- *(deps)* Update dependency fastapi to v0.136.1
- Always return bytearrays to handle album cove correctly
- *(deps)* Update pip to 26.1.1 security
- *(deps)* Update dependency pydantic to v2.13.4
- *(deps)* Update dependency pydantic-settings to v2.14.1
- *(deps)* Pin to 3.14.0
- *(deps)* Update dependency fastapi to v0.136.3
- Show slow log formatting
- Use path for combining paths
- *(deps)* Update dependency fastapi to v0.137.1
- *(deps)* Update dependency fastapi to v0.137.2
- *(deps)* Update dependency fastapi to v0.138.1
- *(deps)* Update dependency plotly.js to v3.6.0
- *(deps)* Update plotly for real

### 💼 Other

- *(deps)* Bump requests from 2.32.5 to 2.33.0
- *(deps)* Bump pygments from 2.19.2 to 2.20.0
- Add ty to dependenxies
- Add qa and deps stage to.makefile
- Add name to pyproject
- Expand pyproject.toml
- Add minimum release age to renovate
- *(deps)* Bump urllib3 from 2.6.3 to 2.7.0
- Add debug level in dev target
- Add environment var for musiclibrary to Dockerfile
- Add env variable for media path
- Add environment variable for media path
- Use extend-select for unused imports
- Use asterisk for all python files in docker
- Pin python version to 3.13
- Add caddyfile for https connection locally
- Add caddy target for local https
- *(deps)* Bump msgpack from 1.2.0 to 1.2.1
- Pin version to Python 3.14.0, no newer version available for Raspberry Pi

### 🚜 Refactor

- Use beets-statistics as singleton via lifecycle manager

### 📚 Documentation

- Create changelog for 1.0.3

### 🎨 Styling

- Change return types to satisfy ty
- Reduce log level, use logger for backend, too
- Better log message

### ⚙️ Miscellaneous Tasks

- Add type check to ci pipeline
- Change order so that pytest starts first in case of existing CVEs
## [1.0.3] - 2026-02-16

### 🚀 Features

- Initial show of recently added albums on the start page
- Refactor albums to macro for reusability
- Render recently added albums as tiles in overview
- Configure logfmt logging
- Show track with lowest bitrate on quality page
- Add cache to all paths
- Add health check endpoint /health for monitoring
- Add a slow log warning on slow queries
- Show quality as violin plot instead of boxplot
- Remove general bar plot
- Clean up multiple genres in genre count and heatmap
- *(plots)* Show heatmap and artist plot larger
- Add explanation of genres
- *(genres)* Skip n/a as genre, list 25 top genres
- Update plotly to 3.3.1 in the JS file

### 🐛 Bug Fixes

- *(deps)* Update dependency plotly.js to v3.1.0
- Rendering of plot on start page
- Add all required fields
- Fix query for recently added albums
- Add all album columns to start page
- Add apitool.py to Dockerfile
- *(deps)* Update dependency plotly.js to v3.1.1
- *(deps)* Update pip to 25.3 to fix CVE
- *(deps)* Update dependency plotly.js to v3.3.0
- *(deps)* Update to FastAPI 0.121.2 SECURITY
- Update starlette to 0.49.3
- Rework uv.lock
- Hide albums without name from the recently added albums list
- *(deps)* Update dependency fastapi to v0.128.0
- *(deps)* Update dependency humanize to v4.15.0
- *(deps)* Update dependency plotly.js to v3.3.1
- *(deps)* Uograde pip to 26.0 security fix
- *(deps)* Update dependency fastapi to v0.128.2
- *(deps)* Update dependency fastapi to v0.128.8
- Show album covers with umlauts or UTF-8 in the path

### 💼 Other

- Deactivate dependabot
- Add .envrc to gitignore
- Add Makefile for common targets
- Specify python version better (3.13 <= x <= 4)
- Add dev and prod targets
- Add local db file to make file
- Enable lock file maintenance to include all updates
- Pin FastAPI version for dependency upgrades
- Pin fastapi version
- Pin versions
- Pin uv version, exclude dev deps and compile bytecode

### 📚 Documentation

- Update changelog
- New changelog format
- Revert to old changelog format

### 🎨 Styling

- Formatting
- Formatting and ruff fixes

### ⚙️ Miscellaneous Tasks

- Add CVE check for pip
- Configure renovate to use best practices
## [1.0.2] - 2025-08-20

### 🚀 Features

- Use pie chart for quality indicator on start page
- Use better album image
- Add duplicate list
- Add list of albums and tracks which are not in MusicBrainz
- Show barcode and link to MB in album overview
- Use responsive layout for plots.
- Responsive menu for mobile devices
- Add boxplot for track quality
- Reduce margin for plots

### 🐛 Bug Fixes

- Dependabot.yml syntax error

### 💼 Other

- Update build version in build.sh
- Fix jumping card on start page by setting vertical align
- Fix title in decades page
- Fix title in genre decade heatmap
- Return empty image if image is not available
- Update python to 3.11 in Docker
- *(deps)* Bump pydantic-settings from 2.7.1 to 2.8.1
- Use Pipfile.lock in Dockerfile
- *(deps)* Bump jinja2 from 3.1.5 to 3.1.6
- *(deps-dev)* Bump ruff from 0.9.4 to 0.11.0
- Fix css loading in case of using a reverse_proxy
- *(deps)* Bump pydantic from 2.10.6 to 2.11.1
- *(deps)* Bump pydantic-settings from 2.8.1 to 2.9.1
- *(deps)* Bump h11 from 0.14.0 to 0.16.0
- *(deps-dev)* Bump pytest from 8.3.4 to 8.4.0
- *(deps)* Bump pydantic-settings from 2.9.1 to 2.10.0
- *(deps-dev)* Bump ruff from 0.11.0 to 0.12.0
- *(deps)* Bump fastapi from 0.115.8 to 0.116.1
- *(deps)* Bump starlette from 0.45.3 to 0.47.2
- Add assignee for renovate bot pull requests
- Migrate to uv
- Add __pycache__ to .gitignore
- Docker file uses uv, too
- Include organize imports with ruff
- Add changelog with git cliff

### 🎨 Styling

- Reformatted file
- Organize imports with ruff

### ⚙️ Miscellaneous Tasks

- Remove fluff in dependabot.yaml
- Add docker to dependabot
- Change pipenv to uv in GitHub actions
## [1.0.1] - 2025-02-18

### 💼 Other

- Add latest tag to docker build
- Fix decade and album plots
## [1.0.0] - 2025-02-18

### 🚀 Features

- Add genre heatmap
- Show album covers in album stats
- Improve CSS
- Add plotly to generate nicer plots
- Show genre counts with plotly
- Show artists count in plotly chart
- Add plotly chart for quality
- Show decades in plotly chart
- Add genre heatmap via plotly
- Genre heatmap with plotly
- Add timeline of added items to beet
- Add plotly to generate nicer plots
- Show genre counts with plotly
- Show artists count in plotly chart
- Add plotly chart for quality
- Show decades in plotly chart
- Add genre heatmap via plotly
- Genre heatmap with plotly
- Add timeline histogram

### 💼 Other

- *(deps-dev)* Bump ruff from 0.6.9 to 0.7.0
- *(deps)* Bump pydantic-settings from 2.5.2 to 2.6.0
- *(deps)* Bump fastapi from 0.115.2 to 0.115.4
- *(deps-dev)* Bump ruff from 0.7.0 to 0.7.1
- *(deps)* Bump pydantic-settings from 2.6.0 to 2.6.1
- *(deps-dev)* Bump ruff from 0.7.1 to 0.7.2
- *(deps-dev)* Bump ruff from 0.7.2 to 0.7.3
- *(deps)* Bump fastapi from 0.115.4 to 0.115.5
- *(deps-dev)* Bump ruff from 0.7.3 to 0.7.4
- *(deps-dev)* Bump ruff from 0.7.4 to 0.8.0
- *(deps)* Bump pydantic from 2.9.2 to 2.10.1
- *(deps)* Bump python-multipart from 0.0.9 to 0.0.18
- *(deps)* Bump pydantic from 2.10.1 to 2.10.2
- *(deps-dev)* Bump ruff from 0.8.0 to 0.8.1
- *(deps-dev)* Bump pytest from 8.3.3 to 8.3.4
- *(deps)* Bump fastapi from 0.115.5 to 0.115.6
- *(deps-dev)* Bump ruff from 0.8.1 to 0.8.2
- *(deps)* Bump pydantic-settings from 2.6.1 to 2.7.0
- *(deps)* Bump pydantic from 2.10.3 to 2.10.4
- *(deps-dev)* Bump ruff from 0.8.2 to 0.8.4
- *(deps)* Bump jinja2 from 3.1.4 to 3.1.5
- *(deps)* Bump pydantic-settings from 2.7.0 to 2.7.1
- *(deps-dev)* Bump ruff from 0.8.4 to 0.8.6
- *(deps-dev)* Bump ruff from 0.8.6 to 0.9.1
- *(deps)* Bump pydantic from 2.10.4 to 2.10.5
- Increase Python version to 3.11
- *(navigation)* Fix navigation header
- Fix animation to start from the beginning of parent
- *(deps-dev)* Bump ruff from 0.9.1 to 0.9.2
- *(deps-dev)* Bump ruff from 0.9.2 to 0.9.4
- *(deps)* Bump fastapi from 0.115.6 to 0.115.8
- *(deps)* Bump pydantic from 2.10.5 to 2.10.6
- *(navigation)* Fix navigation header
- *(deps)* Bump humanize from 4.11.0 to 4.12.0
- Show all artosts and gernews
- *(deps)* Bump humanize from 4.11.0 to 4.12.0
- Show all artosts and gernews

### 📚 Documentation

- *(idea)* Add ideas from alxtrnr@toot.io
- *(ideas)* Clarify and split ideas, mark some as complete

### ⚙️ Miscellaneous Tasks

- Increase Python version to 3.11
- Ignore patch versions of libraries
- Fix dependabot config
## [0.0.1] - 2024-10-16

### 🚀 Features

- Read out database
- First HTML output via FastAPI
- First HTML output via FastAPI
- Top artists shown, general stats page included
- General stats added to homepage
- Use specific exceptions and chains
- Add environment vars for setting the music library path
- Show break down of quality buckets
- Better error messages
- Render quality distribution
- Extend progress bar
- Card design, first draft

### 🐛 Bug Fixes

- Correct syntax on Docker image
- Docker image action syntax

### 💼 Other

- Add musiclibrary.db to gitignore
- Add dockerfile
- *(db)* Expand user directory from config file
- *(dockerfile)* Fixed environment definition
- Add dependabot configuration
- *(deps-dev)* Bump ruff from 0.6.5 to 0.6.7
- *(deps-dev)* Bump ruff from 0.6.7 to 0.6.8
- *(deps)* Bump humanize from 4.10.0 to 4.11.0
- *(deps-dev)* Bump ruff from 0.6.8 to 0.6.9
- Add script to create docker image
- *(deps)* Bump fastapi from 0.115.0 to 0.115.2
- Add .DS_Store to gitignore
- *(deps)* Bump starlette from 0.39.2 to 0.40.0

### 📚 Documentation

- Idea of codecs
- Add docker compose documentation
- First readme with intro and tutorial
- Add screenshots to README
- Format images better
- Fix image path in readme
- Double guerda in namespace

### ⚙️ Miscellaneous Tasks

- Add docker image workflow
- Use correct docker image
- Correct parameter name
- Add login and push
## [initial] - 2024-07-28

### 💼 Other

- Initial dependencies

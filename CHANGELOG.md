## [unreleased]

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

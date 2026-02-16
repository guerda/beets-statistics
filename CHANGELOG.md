# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Add explanation of genres by @guerda
- Add CVE check for pip by @guerda
- Add a slow log warning on slow queries by @guerda
- Add local db file to make file by @guerda
- Add apitool.py to Dockerfile by @guerda
- Add health check endpoint /health for monitoring by @guerda
- Add cache to all paths by @guerda
- Add all album columns to start page by @guerda
- Add all required fields by @guerda
- Add dev and prod targets by @guerda
- Add Makefile for common targets by @guerda
- Add .envrc to gitignore by @guerda

### Changed
- Merge pull request #142 from guerda/fix_umlauts_in_album_cover by @guerda in [#142](https://github.com/guerda/beets-statistics/pull/142)
- Merge pull request #134 from guerda/renovate/python-3.13-slim by @guerda in [#134](https://github.com/guerda/beets-statistics/pull/134)
- Update python:3.13-slim docker digest to 3de9a8d by @renovate[bot]
- Merge pull request #136 from guerda/renovate/ghcr.io-astral-sh-uv-0.x by @guerda in [#136](https://github.com/guerda/beets-statistics/pull/136)
- Update ghcr.io/astral-sh/uv docker tag to v0.10.2 by @renovate[bot]
- Merge pull request #133 from guerda/renovate/fastapi-0.x by @guerda in [#133](https://github.com/guerda/beets-statistics/pull/133)
- Merge pull request #135 from guerda/renovate/lock-file-maintenance by @guerda in [#135](https://github.com/guerda/beets-statistics/pull/135)
- Lock file maintenance by @renovate[bot]
- Merge pull request #131 from guerda/renovate/ghcr.io-astral-sh-uv-0.x by @guerda in [#131](https://github.com/guerda/beets-statistics/pull/131)
- Update ghcr.io/astral-sh/uv docker tag to v0.10.0 by @renovate[bot]
- Merge pull request #132 from guerda/renovate/python-3.13-slim by @guerda in [#132](https://github.com/guerda/beets-statistics/pull/132)
- Update python:3.13-slim docker digest to 49b618b by @renovate[bot]
- Merge pull request #130 from guerda/renovate/fastapi-0.x by @guerda in [#130](https://github.com/guerda/beets-statistics/pull/130)
- Merge pull request #129 from guerda/renovate/ghcr.io-astral-sh-uv-0.x by @guerda in [#129](https://github.com/guerda/beets-statistics/pull/129)
- Update ghcr.io/astral-sh/uv docker tag to v0.9.29 by @renovate[bot]
- Merge pull request #126 from guerda/renovate/python-3.13-slim by @guerda in [#126](https://github.com/guerda/beets-statistics/pull/126)
- Update python:3.13-slim docker digest to 2b9c980 by @renovate[bot]
- Merge pull request #128 from guerda/renovate/ruff-0.x by @guerda in [#128](https://github.com/guerda/beets-statistics/pull/128)
- Update dependency ruff to v0.15.0 by @renovate[bot]
- Merge pull request #127 from guerda/renovate/actions-checkout-digest by @guerda in [#127](https://github.com/guerda/beets-statistics/pull/127)
- Update actions/checkout digest to de0fac2 by @renovate[bot]
- Merge pull request #124 from guerda/renovate/ghcr.io-astral-sh-uv-0.x by @guerda in [#124](https://github.com/guerda/beets-statistics/pull/124)
- Update ghcr.io/astral-sh/uv docker tag to v0.9.28 by @renovate[bot]
- Merge pull request #123 from guerda/renovate/ghcr.io-astral-sh-uv-0.9.27 by @guerda in [#123](https://github.com/guerda/beets-statistics/pull/123)
- Update ghcr.io/astral-sh/uv:0.9.27 docker digest to 143b40f by @renovate[bot]
- Pin uv version, exclude dev deps and compile bytecode by @guerda
- Merge pull request #121 from guerda/renovate/lock-file-maintenance by @guerda in [#121](https://github.com/guerda/beets-statistics/pull/121)
- Lock file maintenance by @renovate[bot]
- Merge pull request #98 from guerda/renovate/plotly.js-3.x by @guerda in [#98](https://github.com/guerda/beets-statistics/pull/98)
- Update plotly to 3.3.1 in the JS file by @guerda
- Merge pull request #120 from guerda/renovate/ruff-0.x by @guerda in [#120](https://github.com/guerda/beets-statistics/pull/120)
- Update dependency ruff to v0.14.14 by @renovate[bot]
- Merge pull request #119 from guerda/renovate/actions-setup-python-digest by @guerda in [#119](https://github.com/guerda/beets-statistics/pull/119)
- Update actions/setup-python digest to a309ff8 by @renovate[bot]
- Merge pull request #116 from guerda/renovate/python-3.13-slim by @guerda in [#116](https://github.com/guerda/beets-statistics/pull/116)
- Update python:3.13-slim docker digest to 51e1a0a by @renovate[bot]
- Merge pull request #117 from guerda/renovate/ghcr.io-astral-sh-uv-latest by @guerda in [#117](https://github.com/guerda/beets-statistics/pull/117)
- Update ghcr.io/astral-sh/uv:latest docker digest to 9a23023 by @renovate[bot]
- Merge pull request #118 from guerda/renovate/ruff-0.x by @guerda in [#118](https://github.com/guerda/beets-statistics/pull/118)
- Update dependency ruff to v0.14.13 by @renovate[bot]
- Merge pull request #115 from guerda/renovate/lock-file-maintenance by @guerda in [#115](https://github.com/guerda/beets-statistics/pull/115)
- Lock file maintenance by @renovate[bot]
- Merge pull request #114 from guerda/renovate/ghcr.io-astral-sh-uv-latest by @guerda in [#114](https://github.com/guerda/beets-statistics/pull/114)
- Update ghcr.io/astral-sh/uv:latest docker digest to 816fdce by @renovate[bot]
- Merge pull request #113 from guerda/renovate/ruff-0.x by @guerda in [#113](https://github.com/guerda/beets-statistics/pull/113)
- Update dependency ruff to v0.14.11 by @renovate[bot]
- Merge pull request #112 from guerda/renovate/ghcr.io-astral-sh-uv-latest by @guerda in [#112](https://github.com/guerda/beets-statistics/pull/112)
- Update ghcr.io/astral-sh/uv:latest docker digest to 2320e6c by @renovate[bot]
- Merge pull request #111 from guerda/feat_genre_top by @guerda in [#111](https://github.com/guerda/beets-statistics/pull/111)
- Skip n/a as genre, list 25 top genres by @guerda
- Merge pull request #110 from guerda/renovate/pin-dependencies by @guerda in [#110](https://github.com/guerda/beets-statistics/pull/110)
- Pin dependencies by @renovate[bot]
- Configure renovate to use best practices by @guerda
- Merge pull request #109 from guerda/renovate/lock-file-maintenance by @guerda in [#109](https://github.com/guerda/beets-statistics/pull/109)
- Lock file maintenance by @renovate[bot]
- Merge pull request #108 from guerda/renovate/humanize-4.x by @guerda in [#108](https://github.com/guerda/beets-statistics/pull/108)
- Merge pull request #107 from guerda/renovate/ruff-0.x by @guerda in [#107](https://github.com/guerda/beets-statistics/pull/107)
- Update dependency ruff to v0.14.10 by @renovate[bot]
- Pin versions by @guerda
- Merge pull request #106 from guerda/renovate/fastapi-0.x by @guerda in [#106](https://github.com/guerda/beets-statistics/pull/106)
- Pin fastapi version by @guerda
- Merge pull request #105 from guerda/build_pin_fastapi by @guerda in [#105](https://github.com/guerda/beets-statistics/pull/105)
- Pin FastAPI version for dependency upgrades by @guerda
- Update changelog by @guerda
- Merge pull request #104 from guerda/feat_larger_heatmap by @guerda in [#104](https://github.com/guerda/beets-statistics/pull/104)
- Show heatmap and artist plot larger by @guerda
- Merge pull request #103 from guerda/fix_multiple_genres by @guerda in [#103](https://github.com/guerda/beets-statistics/pull/103)
- Clean up multiple genres in genre count and heatmap by @guerda
- Merge pull request #101 from guerda/fix_column_name by @guerda in [#101](https://github.com/guerda/beets-statistics/pull/101)
- Merge pull request #99 from guerda/fix_latest_album_na by @guerda in [#99](https://github.com/guerda/beets-statistics/pull/99)
- Merge pull request #100 from guerda/fix_fastapi_bump by @guerda in [#100](https://github.com/guerda/beets-statistics/pull/100)
- Merge pull request #96 from guerda/renovate/lock-file-maintenance by @guerda in [#96](https://github.com/guerda/beets-statistics/pull/96)
- Lock file maintenance by @renovate[bot]
- Merge pull request #94 from guerda/renovate/actions-checkout-6.x by @guerda in [#94](https://github.com/guerda/beets-statistics/pull/94)
- Update actions/checkout action to v6 by @renovate[bot]
- Merge pull request #95 from guerda/guerda-patch-1 by @guerda in [#95](https://github.com/guerda/beets-statistics/pull/95)
- Enable lock file maintenance to include all updates by @guerda
- Merge pull request #93 from guerda/fix_update_starlette by @guerda in [#93](https://github.com/guerda/beets-statistics/pull/93)
- Bump version to 1.0.3 by @guerda
- Merge pull request #92 from guerda/feat_violin by @guerda in [#92](https://github.com/guerda/beets-statistics/pull/92)
- Show quality as violin plot instead of boxplot by @guerda
- Merge pull request #91 from guerda/chore_deps_fastapi by @guerda in [#91](https://github.com/guerda/beets-statistics/pull/91)
- Merge pull request #90 from guerda/chore_logfmter by @guerda in [#90](https://github.com/guerda/beets-statistics/pull/90)
- Chore(deps) update logfmter to 0.0.11 by @guerda
- Merge pull request #87 from guerda/renovate/plotly.js-3.x by @guerda in [#87](https://github.com/guerda/beets-statistics/pull/87)
- Update to plotly 3.3.0 also in the files by @guerda
- Merge pull request #89 from guerda/fix_pip_cve by @guerda in [#89](https://github.com/guerda/beets-statistics/pull/89)
- Merge pull request #86 from guerda/feat_pip_audit by @guerda in [#86](https://github.com/guerda/beets-statistics/pull/86)
- Merge pull request #84 from guerda/renovate/plotly.js-3.x by @guerda in [#84](https://github.com/guerda/beets-statistics/pull/84)
- Update plotly to 3.1.1 by @guerda
- Merge pull request #83 from guerda/feat_slow_log by @guerda in [#83](https://github.com/guerda/beets-statistics/pull/83)
- Merge pull request #82 from guerda/feat_health_endpoint by @guerda in [#82](https://github.com/guerda/beets-statistics/pull/82)
- Merge pull request #81 from guerda/renovate/actions-setup-python-6.x by @guerda in [#81](https://github.com/guerda/beets-statistics/pull/81)
- Update actions/setup-python action to v6 by @renovate[bot]
- Merge pull request #80 from guerda/feat_cache by @guerda in [#80](https://github.com/guerda/beets-statistics/pull/80)
- Formatting and ruff fixes by @guerda
- Merge pull request #77 from guerda/feat_worst_quality by @guerda in [#77](https://github.com/guerda/beets-statistics/pull/77)
- Show track with lowest bitrate on quality page by @guerda
- Merge pull request #76 from guerda/feat_logfmt by @guerda in [#76](https://github.com/guerda/beets-statistics/pull/76)
- Configure logfmt logging by @guerda
- Merge pull request #75 from guerda/feat_recently_added by @guerda in [#75](https://github.com/guerda/beets-statistics/pull/75)
- Render recently added albums as tiles in overview by @guerda
- Refactor albums to macro for reusability by @guerda
- Formatting by @guerda
- Specify python version better (3.13 <= x <= 4) by @guerda
- Initial show of recently added albums on the start page by @guerda
- Delete .github/release-drafter.yml by @guerda
- Deactivate dependabot by @guerda
- Merge pull request #71 from guerda/renovate/plotly.js-3.x by @guerda in [#71](https://github.com/guerda/beets-statistics/pull/71)
- Update plotly.js to 3.1.0 by @guerda
- Merge pull request #70 from guerda/renovate/python-3.x by @guerda in [#70](https://github.com/guerda/beets-statistics/pull/70)
- Update to Python 3.13 everywhere by @guerda
- Update dependency python by @renovate[bot]
- Merge pull request #74 from guerda/renovate/actions-setup-python-5.x by @guerda in [#74](https://github.com/guerda/beets-statistics/pull/74)
- Update actions/setup-python action to v5 by @renovate[bot]
- Merge pull request #73 from guerda/renovate/actions-checkout-5.x by @guerda in [#73](https://github.com/guerda/beets-statistics/pull/73)
- Update actions/checkout action to v5 by @renovate[bot]
- Bump version in build script by @guerda

### Fixed
- Show album covers with umlauts or UTF-8 in the path by @guerda
- Update dependency fastapi to v0.128.8 by @renovate[bot]
- Update dependency fastapi to v0.128.2 by @renovate[bot]
- Uograde pip to 26.0 security fix by @guerda
- Update dependency plotly.js to v3.3.1 by @renovate[bot]
- Update dependency humanize to v4.15.0 by @renovate[bot]
- Update dependency fastapi to v0.128.0 by @renovate[bot]
- Fix column name by @guerda
- Hide albums without name from the recently added albums list by @guerda
- Rework uv.lock by @guerda
- Update starlette to 0.49.3 by @guerda
- Update to FastAPI 0.121.2 SECURITY by @guerda
- Update dependency plotly.js to v3.3.0 by @renovate[bot]
- Update pip to 25.3 to fix CVE by @guerda
- Update dependency plotly.js to v3.1.1 by @renovate[bot]
- Fix query for recently added albums by @guerda
- Rendering of plot on start page by @guerda
- Update dependency plotly.js to v3.1.0 by @renovate[bot]

### Removed
- Remove general bar plot by @guerda

## [1.0.2] - 2025-08-20

### Added
- Add changelog with git cliff by @guerda
- Add __pycache__ to .gitignore by @guerda
- Add assignee for renovate bot pull requests by @guerda
- Add renovate.json by @renovate[bot]
- Add docker to dependabot by @guerda
- Add boxplot for track quality by @guerda
- Add list of albums and tracks which are not in MusicBrainz by @guerda
- Add duplicate list by @guerda

### Changed
- Merge pull request #67 from guerda/build_uv by @guerda in [#67](https://github.com/guerda/beets-statistics/pull/67)
- Organize imports with ruff by @guerda
- Include organize imports with ruff by @guerda
- Reformatted file by @guerda
- Change pipenv to uv in GitHub actions by @guerda
- Docker file uses uv, too by @guerda
- Migrate to uv by @guerda
- Merge pull request #69 from guerda/renovate/configure by @guerda in [#69](https://github.com/guerda/beets-statistics/pull/69)
- Merge pull request #66 from guerda/dependabot/pip/starlette-0.47.2 by @guerda in [#66](https://github.com/guerda/beets-statistics/pull/66)
- Bump starlette from 0.45.3 to 0.47.2 by @dependabot[bot]
- Merge pull request #65 from guerda/dependabot/pip/fastapi-0.116.1 by @guerda in [#65](https://github.com/guerda/beets-statistics/pull/65)
- Bump fastapi from 0.115.8 to 0.116.1 by @dependabot[bot]
- Merge pull request #64 from guerda/dependabot/pip/ruff-0.12.0 by @guerda in [#64](https://github.com/guerda/beets-statistics/pull/64)
- Bump ruff from 0.11.0 to 0.12.0 by @dependabot[bot]
- Merge pull request #63 from guerda/dependabot/pip/pydantic-settings-2.10.0 by @guerda in [#63](https://github.com/guerda/beets-statistics/pull/63)
- Bump pydantic-settings from 2.9.1 to 2.10.0 by @dependabot[bot]
- Merge pull request #62 from guerda/dependabot/pip/pytest-8.4.0 by @guerda in [#62](https://github.com/guerda/beets-statistics/pull/62)
- Bump pytest from 8.3.4 to 8.4.0 by @dependabot[bot]
- Merge pull request #61 from guerda/dependabot/pip/h11-0.16.0 by @guerda in [#61](https://github.com/guerda/beets-statistics/pull/61)
- Bump h11 from 0.14.0 to 0.16.0 by @dependabot[bot]
- Merge pull request #60 from guerda/dependabot/pip/pydantic-settings-2.9.1 by @guerda in [#60](https://github.com/guerda/beets-statistics/pull/60)
- Bump pydantic-settings from 2.8.1 to 2.9.1 by @dependabot[bot]
- Merge pull request #59 from guerda/dependabot/pip/pydantic-2.11.1 by @guerda in [#59](https://github.com/guerda/beets-statistics/pull/59)
- Bump pydantic from 2.10.6 to 2.11.1 by @dependabot[bot]
- Merge pull request #58 from guerda/dependabot/pip/ruff-0.11.0 by @guerda in [#58](https://github.com/guerda/beets-statistics/pull/58)
- Bump ruff from 0.9.4 to 0.11.0 by @dependabot[bot]
- Reduce margin for plots by @guerda
- Merge pull request #55 from guerda/dependabot/pip/jinja2-3.1.6 by @guerda in [#55](https://github.com/guerda/beets-statistics/pull/55)
- Bump jinja2 from 3.1.5 to 3.1.6 by @dependabot[bot]
- Responsive menu for mobile devices by @guerda
- Use Pipfile.lock in Dockerfile by @guerda
- Merge pull request #54 from guerda/dependabot/pip/pydantic-settings-2.8.1 by @guerda in [#54](https://github.com/guerda/beets-statistics/pull/54)
- Bump pydantic-settings from 2.7.1 to 2.8.1 by @dependabot[bot]
- Use responsive layout for plots. by @guerda
- Show barcode and link to MB in album overview by @guerda
- Update python to 3.11 in Docker by @guerda
- Merge pull request #53 from guerda/feat-duplicates by @guerda in [#53](https://github.com/guerda/beets-statistics/pull/53)
- Merge pull request #51 from guerda/small-bug-fixes by @guerda in [#51](https://github.com/guerda/beets-statistics/pull/51)
- Return empty image if image is not available by @guerda
- Use better album image by @guerda
- Use pie chart for quality indicator on start page by @guerda
- Update build version in build.sh by @guerda

### Fixed
- Fix css loading in case of using a reverse_proxy by @guerda
- Dependabot.yml syntax error by @guerda
- Fix title in genre decade heatmap by @guerda
- Fix title in decades page by @guerda
- Fix jumping card on start page by setting vertical align by @guerda

### Removed
- Remove fluff in dependabot.yaml by @guerda

## [1.0.1] - 2025-02-18

### Added
- Add latest tag to docker build by @guerda

### Fixed
- Fix decade and album plots by @guerda

## [1.0.0] - 2025-02-18

### Added
- Add timeline histogram by @guerda
- Add debugging by @guerda
- Add genre heatmap via plotly by @guerda
- Add plotly chart for quality by @guerda
- Add plotly to generate nicer plots by @guerda
- Add timeline of added items to beet by @guerda
- Add debugging by @guerda
- Add genre heatmap via plotly by @guerda
- Add plotly chart for quality by @guerda
- Add plotly to generate nicer plots by @guerda
- Add genre heatmap by @guerda
- Add release drafter config by @guerda
- Add ideas from alxtrnr@toot.io by @guerda

### Changed
- Merge pull request #50 from guerda/feat-added-timeline by @guerda in [#50](https://github.com/guerda/beets-statistics/pull/50)
- Genre heatmap with plotly by @guerda
- Show all artosts and gernews by @guerda
- Show decades in plotly chart by @guerda
- Show artists count in plotly chart by @guerda
- Show genre counts with plotly by @guerda
- Merge pull request #49 from guerda/feat-plotly by @guerda in [#49](https://github.com/guerda/beets-statistics/pull/49)
- Genre heatmap with plotly by @guerda
- Bump humanize from 4.11.0 to 4.12.0 by @dependabot[bot]
- Show all artosts and gernews by @guerda
- Show decades in plotly chart by @guerda
- Show artists count in plotly chart by @guerda
- Show genre counts with plotly by @guerda
- Merge pull request #48 from guerda/dependabot/pip/humanize-4.12.0 by @guerda in [#48](https://github.com/guerda/beets-statistics/pull/48)
- Bump humanize from 4.11.0 to 4.12.0 by @dependabot[bot]
- Merge pull request #47 from guerda/css-tweaks by @guerda in [#47](https://github.com/guerda/beets-statistics/pull/47)
- Merge branch 'main' into css-tweaks by @guerda
- Improve CSS by @guerda
- Ignore patch versions of libraries by @guerda
- Merge pull request #42 from guerda/dependabot/pip/pydantic-2.10.6 by @guerda in [#42](https://github.com/guerda/beets-statistics/pull/42)
- Bump pydantic from 2.10.5 to 2.10.6 by @dependabot[bot]
- Merge pull request #45 from guerda/dependabot/pip/fastapi-0.115.8 by @guerda in [#45](https://github.com/guerda/beets-statistics/pull/45)
- Bump fastapi from 0.115.6 to 0.115.8 by @dependabot[bot]
- Merge pull request #46 from guerda/dependabot/pip/ruff-0.9.4 by @guerda in [#46](https://github.com/guerda/beets-statistics/pull/46)
- Bump ruff from 0.9.2 to 0.9.4 by @dependabot[bot]
- Merge pull request #41 from guerda/dependabot/pip/ruff-0.9.2 by @guerda in [#41](https://github.com/guerda/beets-statistics/pull/41)
- Bump ruff from 0.9.1 to 0.9.2 by @dependabot[bot]
- Merge pull request #40 from guerda/feat-cover-art by @guerda in [#40](https://github.com/guerda/beets-statistics/pull/40)
- Show album covers in album stats by @guerda
- Fix animation to start from the beginning of parent by @guerda
- Increase Python version to 3.11 by @guerda
- Merge pull request #39 from guerda/feat_genre_heatmap by @guerda in [#39](https://github.com/guerda/beets-statistics/pull/39)
- Increase Python version to 3.11 by @guerda
- Merge pull request #38 from guerda/dependabot/pip/pydantic-2.10.5 by @guerda in [#38](https://github.com/guerda/beets-statistics/pull/38)
- Bump pydantic from 2.10.4 to 2.10.5 by @dependabot[bot]
- Merge pull request #37 from guerda/dependabot/pip/ruff-0.9.1 by @guerda in [#37](https://github.com/guerda/beets-statistics/pull/37)
- Bump ruff from 0.8.6 to 0.9.1 by @dependabot[bot]
- Merge pull request #33 from guerda/dependabot/pip/ruff-0.8.6 by @guerda in [#33](https://github.com/guerda/beets-statistics/pull/33)
- Bump ruff from 0.8.4 to 0.8.6 by @dependabot[bot]
- Merge pull request #34 from guerda/dependabot/pip/pydantic-settings-2.7.1 by @guerda in [#34](https://github.com/guerda/beets-statistics/pull/34)
- Bump pydantic-settings from 2.7.0 to 2.7.1 by @dependabot[bot]
- Merge pull request #31 from guerda/dependabot/pip/jinja2-3.1.5 by @guerda in [#31](https://github.com/guerda/beets-statistics/pull/31)
- Bump jinja2 from 3.1.4 to 3.1.5 by @dependabot[bot]
- Merge pull request #30 from guerda/dependabot/pip/ruff-0.8.4 by @guerda in [#30](https://github.com/guerda/beets-statistics/pull/30)
- Bump ruff from 0.8.2 to 0.8.4 by @dependabot[bot]
- Merge pull request #29 from guerda/dependabot/pip/pydantic-2.10.4 by @guerda in [#29](https://github.com/guerda/beets-statistics/pull/29)
- Bump pydantic from 2.10.3 to 2.10.4 by @dependabot[bot]
- Merge pull request #28 from guerda/dependabot/pip/pydantic-settings-2.7.0 by @guerda in [#28](https://github.com/guerda/beets-statistics/pull/28)
- Bump pydantic-settings from 2.6.1 to 2.7.0 by @dependabot[bot]
- Merge pull request #25 from guerda/dependabot/pip/ruff-0.8.2 by @guerda in [#25](https://github.com/guerda/beets-statistics/pull/25)
- Bump ruff from 0.8.1 to 0.8.2 by @dependabot[bot]
- Merge pull request #24 from guerda/dependabot/pip/fastapi-0.115.6 by @guerda in [#24](https://github.com/guerda/beets-statistics/pull/24)
- Bump fastapi from 0.115.5 to 0.115.6 by @dependabot[bot]
- Merge pull request #20 from guerda/dependabot/pip/pytest-8.3.4 by @guerda in [#20](https://github.com/guerda/beets-statistics/pull/20)
- Bump pytest from 8.3.3 to 8.3.4 by @dependabot[bot]
- Merge pull request #21 from guerda/dependabot/pip/ruff-0.8.1 by @guerda in [#21](https://github.com/guerda/beets-statistics/pull/21)
- Bump ruff from 0.8.0 to 0.8.1 by @dependabot[bot]
- Merge pull request #22 from guerda/dependabot/pip/pydantic-2.10.2 by @guerda in [#22](https://github.com/guerda/beets-statistics/pull/22)
- Bump pydantic from 2.10.1 to 2.10.2 by @dependabot[bot]
- Merge pull request #23 from guerda/dependabot/pip/python-multipart-0.0.18 by @guerda in [#23](https://github.com/guerda/beets-statistics/pull/23)
- Bump python-multipart from 0.0.9 to 0.0.18 by @dependabot[bot]
- Merge pull request #19 from guerda/dependabot/pip/pydantic-2.10.1 by @guerda in [#19](https://github.com/guerda/beets-statistics/pull/19)
- Bump pydantic from 2.9.2 to 2.10.1 by @dependabot[bot]
- Merge pull request #18 from guerda/dependabot/pip/ruff-0.8.0 by @guerda in [#18](https://github.com/guerda/beets-statistics/pull/18)
- Bump ruff from 0.7.4 to 0.8.0 by @dependabot[bot]
- Merge pull request #16 from guerda/dependabot/pip/ruff-0.7.4 by @guerda in [#16](https://github.com/guerda/beets-statistics/pull/16)
- Bump ruff from 0.7.3 to 0.7.4 by @dependabot[bot]
- Merge pull request #17 from guerda/dependabot/pip/fastapi-0.115.5 by @guerda in [#17](https://github.com/guerda/beets-statistics/pull/17)
- Bump fastapi from 0.115.4 to 0.115.5 by @dependabot[bot]
- Merge pull request #15 from guerda/dependabot/pip/ruff-0.7.3 by @guerda in [#15](https://github.com/guerda/beets-statistics/pull/15)
- Bump ruff from 0.7.2 to 0.7.3 by @dependabot[bot]
- Merge pull request #13 from guerda/dependabot/pip/ruff-0.7.2 by @guerda in [#13](https://github.com/guerda/beets-statistics/pull/13)
- Bump ruff from 0.7.1 to 0.7.2 by @dependabot[bot]
- Merge pull request #14 from guerda/dependabot/pip/pydantic-settings-2.6.1 by @guerda in [#14](https://github.com/guerda/beets-statistics/pull/14)
- Bump pydantic-settings from 2.6.0 to 2.6.1 by @dependabot[bot]
- Merge pull request #10 from guerda/dependabot/pip/ruff-0.7.1 by @guerda in [#10](https://github.com/guerda/beets-statistics/pull/10)
- Bump ruff from 0.7.0 to 0.7.1 by @dependabot[bot]
- Merge pull request #11 from guerda/dependabot/pip/fastapi-0.115.4 by @guerda in [#11](https://github.com/guerda/beets-statistics/pull/11)
- Bump fastapi from 0.115.2 to 0.115.4 by @dependabot[bot]
- Merge pull request #8 from guerda/dependabot/pip/pydantic-settings-2.6.0 by @guerda in [#8](https://github.com/guerda/beets-statistics/pull/8)
- Bump pydantic-settings from 2.5.2 to 2.6.0 by @dependabot[bot]
- Merge pull request #9 from guerda/dependabot/pip/ruff-0.7.0 by @guerda in [#9](https://github.com/guerda/beets-statistics/pull/9)
- Bump ruff from 0.6.9 to 0.7.0 by @dependabot[bot]
- Clarify and split ideas, mark some as complete by @guerda

### Fixed
- Fix return value for get_track_decades() by @guerda
- Fix return value for get_track_decades() by @guerda
- Fix navigation header by @guerda
- Fix dependabot config by @guerda
- Fix navigation header by @guerda

## [0.0.1] - 2024-10-16

### Added
- Add login and push by @guerda
- Add docker image workflow by @guerda
- Add screenshots to README by @guerda
- Add .DS_Store to gitignore by @guerda
- Add script to create docker image by @guerda
- Add dependabot configuration by @guerda
- Add docker compose documentation by @guerda
- Add environment vars for setting the music library path by @guerda
- Add dockerfile by @guerda
- Add musiclibrary.db to gitignore by @guerda

### Changed
- Double guerda in namespace by @guerda
- Merge pull request #7 from guerda/dependabot/pip/starlette-0.40.0 by @guerda in [#7](https://github.com/guerda/beets-statistics/pull/7)
- Bump starlette from 0.39.2 to 0.40.0 by @dependabot[bot]
- Correct parameter name by @guerda
- Use correct docker image by @guerda
- Format images better by @guerda
- Merge pull request #6 from guerda/dependabot/pip/fastapi-0.115.2 by @guerda in [#6](https://github.com/guerda/beets-statistics/pull/6)
- Bump fastapi from 0.115.0 to 0.115.2 by @dependabot[bot]
- Create LICENSE by @guerda
- Merge pull request #5 from guerda/doc_readme by @guerda in [#5](https://github.com/guerda/beets-statistics/pull/5)
- Update README.md by @guerda
- First readme with intro and tutorial by @guerda
- UI polishing by @guerda
- UI polishing of data tables by @guerda
- Card design, first draft by @guerda
- Merge pull request #3 from guerda/dependabot/pip/ruff-0.6.9 by @guerda in [#3](https://github.com/guerda/beets-statistics/pull/3)
- Bump ruff from 0.6.8 to 0.6.9 by @dependabot[bot]
- Merge pull request #4 from guerda/dependabot/pip/humanize-4.11.0 by @guerda in [#4](https://github.com/guerda/beets-statistics/pull/4)
- Bump humanize from 4.10.0 to 4.11.0 by @dependabot[bot]
- Merge pull request #2 from guerda/dependabot/pip/ruff-0.6.8 by @guerda in [#2](https://github.com/guerda/beets-statistics/pull/2)
- Bump ruff from 0.6.7 to 0.6.8 by @dependabot[bot]
- Merge pull request #1 from guerda/dependabot/pip/ruff-0.6.7 by @guerda in [#1](https://github.com/guerda/beets-statistics/pull/1)
- Bump ruff from 0.6.5 to 0.6.7 by @dependabot[bot]
- Create python-app.yml by @guerda
- Update ideas.md by @guerda
- Extend progress bar by @guerda
- Render quality distribution by @guerda
- Better error messages by @guerda
- Show break down of quality buckets by @guerda
- Use specific exceptions and chains by @guerda
- Idea of codecs by @guerda
- Expand user directory from config file by @guerda
- General stats added to homepage by @guerda
- Top artists shown, general stats page included by @guerda
- First HTML output via FastAPI by @guerda
- First HTML output via FastAPI by @guerda
- Read out database by @guerda

### Fixed
- Fix image path in readme by @guerda
- Docker image action syntax by @guerda
- Correct syntax on Docker image by @guerda
- Fixed environment definition by @guerda

### New Contributors
* @dependabot[bot] made their first contribution

## [initial] - 2024-07-28

### Changed
- Initial dependencies by @guerda

### New Contributors
* @guerda made their first contribution

[unreleased]: https://github.com/guerda/beets-statistics/compare/v1.0.2...HEAD
[1.0.2]: https://github.com/guerda/beets-statistics/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/guerda/beets-statistics/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/guerda/beets-statistics/compare/v0.0.1...v1.0.0
[0.0.1]: https://github.com/guerda/beets-statistics/compare/initial...v0.0.1

<!-- generated by git-cliff -->

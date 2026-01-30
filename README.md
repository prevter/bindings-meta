# Geometry Dash Bindings Cache
[![Rebuild codegen](https://github.com/Prevter/bindings-meta/actions/workflows/build.yml/badge.svg)](https://github.com/Prevter/bindings-meta/actions/workflows/build.yml)

Simple github workflow script that periodically checks the [Geode bindings repo](https://github.com/geode-sdk/bindings), and uploads all function offsets from it.

Bindings are generated for:
- **Windows**: 2.204, 2.206, 2.2074, 2.2081
- **macOS**: 2.200 (intel only), 2.206, 2.2074, 2.2081
- **iOS**: 2.206, 2.2074, 2.2081

In addition, the script also adds some custom bindings for entry points and STL functions, which are not present in the bingings repo. 
(if you want to add more, feel free to make a PR to files in `extras` directory)

(with game updates, this list will be expanded)

This repo is used by [BetterCrashlogs mod](https://github.com/Prevter/BetterCrashlogs) to keep the bindings always up-to-date (+ support multiple game versions)

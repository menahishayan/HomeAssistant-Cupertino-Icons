# HomeAssistant-Cupertino-Icons Build-Tools

This is the dev branch used to build and release new versions of this repo.

## Build Instructions
1. Download SF Symbols Viewer from Apple
2. Select all modifyable symbols (non-copyrighted and available for use with modification) and export them
3. Run `python3 ./build-tools/extractRegular<version>.py` from the root directory to export only a single symbol from each SVG iconset
4. SVG cleanup setup:  
  - Edit `./build-tools/ResizeAllArtboards.jsx` and `./build-tools/ScaleDown.jsx` as follows:
    - requiredABsize, OPTIONS.size, OPTIONS.height and OPTIONS.width = 24 (v2)
    - requiredABsize, OPTIONS.size, OPTIONS.height and OPTIONS.width = 512 (v3+)
  - Copy `./build-tools/ResizeAllArtboards.jsx` and `./build-tools/ScaleDown.jsx` into `<Adobe Illustrator Path>/Presets/<language>/Scripts/`
  - Open Illustrator
  - Window > Actions > Create New Action from menu item > :
    - Fit to artwork bounds
    - ScaleDown
    - ResizeAllArtboards
5. Actual SVG cleanup:
  - Open Illustrator
  - Window > Actions > Select your new action:
  - Window > Actions > Batch:
    - Select the folders for input and output
  - Run the batch operation to properly scale and align all SVG items
6. To generate dist file (v2 and below) run `python3 ./build-tools/generate<version>.py` to get a js file with all the SVG paths. Done
7. **OR** Restore color data (v3+)
  - SF Symbols 3+ supports multicolor icons, but Illustrator strips the color class names. To restore them, run `python3 ./build-tools/refillColors.py`
8. Move finalized SVGs to custom_components/cupertino/data/ios

import os

base = os.path.expanduser("~/Lego Website/Lego-Photography-Interactive-Portfolio")
os.chdir(base)

with open("_sass/_map.scss") as f:
    map_scss = f.read()

old_block = '''#map {
  background-color: #0d1117;
  border: 2px solid rgba(123, 198, 255, 0.35);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(123, 198, 255, 0.1), 0 12px 40px rgba(0, 0, 0, 0.55);
  height: 300px;
  padding: 20px;
  box-sizing: border-box; 
}'''

new_block = '''#map {
  background-color: #0d1117;
  border: 2px solid rgba(123, 198, 255, 0.35);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 0 0 1px rgba(123, 198, 255, 0.1), 0 12px 40px rgba(0, 0, 0, 0.55);
  width: 100%;
  height: clamp(480px, 70vh, 750px);
  height: clamp(480px, 70dvh, 750px);
  box-sizing: border-box;
}'''

if old_block in map_scss:
    map_scss = map_scss.replace(old_block, new_block)
    with open("_sass/_map.scss", "w") as f:
        f.write(map_scss)
    print("_map.scss updated.")
else:
    print("WARNING: #map block not found as expected in _map.scss, check manually.")

with open("map.md") as f:
    content = f.read()

content = content.replace(
    '<div id="map" style="width: 100%; height: clamp(500px, 75vh, 900px);"></div>',
    '<div id="map"></div>'
)

old_load = '''  window.addEventListener('load', function() {
    map.invalidateSize();
    if (clusters.getLayers().length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  });'''

new_load = '''  window.addEventListener('load', function() {
    map.invalidateSize();
    if (clusters.getLayers().length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  });

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      map.invalidateSize();
    }, 150);
  });'''

if old_load in content:
    content = content.replace(old_load, new_load)
    with open("map.md", "w") as f:
        f.write(content)
    print("map.md updated.")
else:
    print("WARNING: load handler block not found as expected in map.md, check manually.")

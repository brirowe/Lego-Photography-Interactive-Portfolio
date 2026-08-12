import os

base = os.path.expanduser("~/Lego Website/Lego-Photography-Interactive-Portfolio")
os.chdir(base)

with open("map.md") as f:
    content = f.read()

old_fit = '''    if (groups.length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  }'''

new_fit = '''    if (filtered.length) {
      var primaryPoints = filtered.filter(function(p) { return p.lng < -50; });
      var basisPoints = primaryPoints.length ? primaryPoints : filtered;
      var bounds = L.latLngBounds(basisPoints.map(function(p) { return [p.lat, p.lng]; }));
      map.fitBounds(bounds, { padding: [30, 30], maxZoom: 12 });
    }
  }'''

if old_fit in content:
    content = content.replace(old_fit, new_fit)
    print("renderMarkers() bounds logic updated.")
else:
    print("WARNING: could not find renderMarkers fitBounds block, check manually.")

old_load = '''  window.addEventListener('load', function() {
    map.invalidateSize();
    if (clusters.getLayers().length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  });'''

new_load = '''  window.addEventListener('load', function() {
    map.invalidateSize();
    renderMarkers();
  });'''

if old_load in content:
    content = content.replace(old_load, new_load)
    print("load handler updated.")
else:
    print("WARNING: could not find load handler block, check manually.")

with open("map.md", "w") as f:
    f.write(content)

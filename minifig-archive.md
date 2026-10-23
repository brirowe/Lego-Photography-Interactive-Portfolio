---
layout: default
title: Minifig Archive
permalink: /minifig-archive/
text_width: false
---

<h1>Minifig Archive</h1>
<p class="archive-intro">Browse every minifig photo below, or use the filters to find something specific.</p>

<div class="archive-filter-bar" id="archive-filter-bar"></div>
<div class="archive-filter-panel" id="archive-filter-panel"></div>
<div class="archive-active-chips" id="archive-active-chips"></div>

<div class="archive-toolbar">
	<span id="archive-count"></span>
</div>

<div class="archive-grid" id="archive-grid"></div>

{% include photo-lightbox.html page="archive" %}

<script>
	const archivePhotos = PHOTO_DATA;
	const baseurl = "{{ site.baseurl }}";

	// Elevation ranges for the Elevation filter (feet)
	var ELEV_BANDS = [
		[5000, 'Under 5,000 ft'],
		[8000, '5,000 to 8,000 ft'],
		[10000, '8,000 to 10,000 ft'],
		[12000, '10,000 to 12,000 ft'],
		[13000, '12,000 to 13,000 ft'],
		[14000, '13,000 to 14,000 ft'],
		[Infinity, '14,000+ ft']
	];
	var ELEV_ORDER = ELEV_BANDS.map(function(b) { return b[1]; });
	function elevBand(ft) {
		if (ft === '' || ft == null || isNaN(ft)) return '';
		ft = Number(ft);
		for (var i = 0; i < ELEV_BANDS.length; i++) {
			if (ft < ELEV_BANDS[i][0]) return ELEV_BANDS[i][1];
		}
	}

	const filterConfig = [
		{ key: 'theme', label: 'Theme' },
		{ key: 'subtheme', label: 'Subtheme' },
		{ key: 'set', label: 'Set Number' },
		{ key: 'year', label: 'Year' },
		{ key: 'season', label: 'Season' },
		{ key: 'background_type', label: 'Background' },
		{ key: 'country', label: 'Country' },
		{ key: 'state', label: 'State' },
		{ key: 'elevation_band', label: 'Elevation', order: ELEV_ORDER }
	];

	// Each filter value as a list, so a photo with two figs (like "Star Wars, Agents")
	// shows up under both
	archivePhotos.forEach(function(p) {
		p.elevation_band = elevBand(p.elevation_ft);
		p.tok = {};
		filterConfig.forEach(function(cfg) { p.tok[cfg.key] = photoTokens(p[cfg.key]); });
	});

	const selected = {};
	filterConfig.forEach(function(c) { selected[c.key] = new Set(); });

	let openCategory = null;

	function matchesExcluding(photo, excludeKey) {
		return filterConfig.every(function(cfg) {
			if (cfg.key === excludeKey) return true;
			const chosen = selected[cfg.key];
			if (chosen.size === 0) return true;
			return photo.tok[cfg.key].some(function(t) { return chosen.has(t); });
		});
	}

	function uniqueValues(key, order) {
		const vals = new Set();
		archivePhotos.forEach(function(p) {
			if (!matchesExcluding(p, key)) return;
			p.tok[key].forEach(function(t) { vals.add(t); });
		});
		const arr = Array.from(vals);
		if (order) {
			return arr.sort(function(a, b) { return order.indexOf(a) - order.indexOf(b); });
		}
		const numeric = arr.every(function(v) { return !isNaN(v); });
		arr.sort(function(a, b) {
			return numeric ? (Number(a) - Number(b)) : a.localeCompare(b);
		});
		return arr;
	}

	function renderFilterBar() {
		const bar = document.getElementById('archive-filter-bar');
		bar.innerHTML = '';

		filterConfig.forEach(function(cfg) {
			const count = selected[cfg.key].size;
			const btn = document.createElement('button');
			btn.type = 'button';
			btn.className = 'filter-toggle' + (openCategory === cfg.key ? ' open' : '') + (count ? ' has-selection' : '');
			btn.innerHTML = cfg.label + (count ? ' <span class="filter-toggle-count">' + count + '</span>' : '') + ' <span class="filter-toggle-arrow">▾</span>';
			btn.addEventListener('click', function() {
				openCategory = openCategory === cfg.key ? null : cfg.key;
				renderFilterBar();
				renderFilterPanel();
			});
			bar.appendChild(btn);
		});
	}

	function renderFilterPanel() {
		const panel = document.getElementById('archive-filter-panel');
		panel.innerHTML = '';
		if (!openCategory) {
			panel.classList.remove('visible');
			return;
		}
		panel.classList.add('visible');

		const cfg = filterConfig.find(function(c) { return c.key === openCategory; });
		const values = uniqueValues(cfg.key, cfg.order);

		const pillWrap = document.createElement('div');
		pillWrap.className = 'filter-pills';

		values.forEach(function(val) {
			const pill = document.createElement('button');
			pill.type = 'button';
			pill.className = 'filter-pill';
			if (selected[cfg.key].has(val)) pill.classList.add('active');
			pill.textContent = val;
			pill.addEventListener('click', function() {
				if (selected[cfg.key].has(val)) {
					selected[cfg.key].delete(val);
				} else {
					selected[cfg.key].add(val);
				}
				renderFilterBar();
				renderActiveChips();
				renderGrid();
				pill.classList.toggle('active');
			});
			pillWrap.appendChild(pill);
		});

		panel.appendChild(pillWrap);
	}

	function renderActiveChips() {
		const container = document.getElementById('archive-active-chips');
		container.innerHTML = '';

		let any = false;
		filterConfig.forEach(function(cfg) {
			selected[cfg.key].forEach(function(val) {
				any = true;
				const chip = document.createElement('button');
				chip.type = 'button';
				chip.className = 'active-chip';
				chip.innerHTML = '<span class="active-chip-label">' + cfg.label + ':</span> ' + val + ' <span class="active-chip-remove">&times;</span>';
				chip.addEventListener('click', function() {
					selected[cfg.key].delete(val);
					renderFilterBar();
					renderFilterPanel();
					renderActiveChips();
					renderGrid();
				});
				container.appendChild(chip);
			});
		});

		if (any) {
			const clearAll = document.createElement('button');
			clearAll.type = 'button';
			clearAll.className = 'clear-all-chip';
			clearAll.textContent = 'Clear all';
			clearAll.addEventListener('click', function() {
				filterConfig.forEach(function(c) { selected[c.key].clear(); });
				renderFilterBar();
				renderFilterPanel();
				renderActiveChips();
				renderGrid();
			});
			container.appendChild(clearAll);
		}
	}

	function matches(photo) {
		return matchesExcluding(photo, null);
	}

	function renderGrid() {
		const grid = document.getElementById('archive-grid');

		// one tile per shot (near-duplicate versions grouped), mixed by theme
		const groups = mixOrder(groupPhotos(archivePhotos.filter(matches)));

		document.getElementById('archive-count').textContent =
			groups.length + (groups.length === 1 ? ' photo' : ' photos');

		grid.innerHTML = '';
		groups.forEach(function(g) {
			const p = g[0];
			const files = g.map(function(x) { return x.filename; });

			const item = document.createElement('div');
			item.className = 'archive-item';
			item.dataset.files = files.join('|');

			const img = document.createElement('img');
			img.loading = 'lazy';
			img.src = baseurl + '/photos/photos_compressed/' + p.filename;
			img.alt = p.theme;
			item.appendChild(img);
			item.addEventListener('click', function() { openPhoto(p.filename, files); });

			if (g.length > 1) {
				const badge = document.createElement('span');
				badge.className = 'version-badge';
				badge.textContent = g.length;
				badge.title = g.length + ' versions';
				item.appendChild(badge);
			}

			const caption = document.createElement('div');
			caption.className = 'archive-caption';
			caption.textContent = [p.theme, p.set, p.year].filter(function(v) { return v && v !== 'None'; }).join(' · ');
			item.appendChild(caption);

			grid.appendChild(item);
		});
	}

	renderFilterBar();
	renderFilterPanel();
	renderActiveChips();
	renderGrid();

	// Arrived from another page: scroll to that photo's tile and open that version
	if (linkedPhoto) {
		const target = Array.from(document.querySelectorAll('.archive-item')).find(function(el) {
			return el.dataset.files.split('|').indexOf(linkedPhoto) !== -1;
		});
		if (target) {
			showLinked(target);
			openPhoto(linkedPhoto, target.dataset.files.split('|'));
		} else {
			openPhoto(linkedPhoto);
		}
	}
</script>
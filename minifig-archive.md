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

<div id="lightbox-overlay" onclick="this.style.display='none'">
	<img id="lightbox-img" src="">
</div>

<script>
	const archivePhotos = {{ site.data.minifig_archive | jsonify }};
	const baseurl = "{{ site.baseurl }}";

	function showLightbox(src) {
		document.getElementById('lightbox-img').src = src;
		document.getElementById('lightbox-overlay').style.display = 'flex';
	}

	archivePhotos.forEach(function(p) {
		p.setTokens = (p.set || '').split(',').map(function(s) { return s.trim(); }).filter(Boolean);
	});

	const filterConfig = [
		{ key: 'theme', label: 'Theme' },
		{ key: 'subtheme', label: 'Subtheme' },
		{ key: 'set', label: 'Set Number', multiToken: true },
		{ key: 'year', label: 'Year' },
		{ key: 'season', label: 'Season' },
		{ key: 'background_type', label: 'Background' }
	];

	const selected = {};
	filterConfig.forEach(function(c) { selected[c.key] = new Set(); });

	let openCategory = null;

	function uniqueValues(key, multiToken) {
		const vals = new Set();
		archivePhotos.forEach(function(p) {
			if (multiToken) {
				p.setTokens.forEach(function(t) { if (t) vals.add(t); });
			} else if (p[key]) {
				vals.add(p[key]);
			}
		});
		const arr = Array.from(vals);
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
		const values = uniqueValues(cfg.key, cfg.multiToken);

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
		return filterConfig.every(function(cfg) {
			const chosen = selected[cfg.key];
			if (chosen.size === 0) return true;
			if (cfg.multiToken) {
				return photo.setTokens.some(function(t) { return chosen.has(t); });
			}
			return chosen.has(photo[cfg.key]);
		});
	}

	function renderGrid() {
		const grid = document.getElementById('archive-grid');
		const filtered = archivePhotos.filter(matches);

		filtered.sort(function(a, b) {
			return (a.theme || '').localeCompare(b.theme || '') || (a.subtheme || '').localeCompare(b.subtheme || '');
		});

		document.getElementById('archive-count').textContent =
			filtered.length + (filtered.length === 1 ? ' photo' : ' photos');

		grid.innerHTML = '';
		filtered.forEach(function(p) {
			const item = document.createElement('div');
			item.className = 'archive-item';

			const img = document.createElement('img');
			img.loading = 'lazy';
			img.src = baseurl + '/photos/photos_compressed/' + p.filename;
			img.alt = p.theme;
			img.addEventListener('click', function() { showLightbox(img.src); });
			item.appendChild(img);

			const caption = document.createElement('div');
			caption.className = 'archive-caption';
			caption.textContent = [p.theme, p.set, p.year].filter(Boolean).join(' · ');
			item.appendChild(caption);

			grid.appendChild(item);
		});
	}

	renderFilterBar();
	renderFilterPanel();
	renderActiveChips();
	renderGrid();
</script>

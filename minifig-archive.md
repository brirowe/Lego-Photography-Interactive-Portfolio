---
layout: default
title: Minifig Archive
permalink: /minifig-archive/
text_width: false
---

<h1>Minifig Archive</h1>
<p class="archive-intro">Browse every minifig photo below, or use the filters to find something specific.</p>

<div class="archive-filters" id="archive-filters"></div>

<div class="archive-toolbar">
	<span id="archive-count"></span>
	<button id="clear-filters" class="clear-filters-btn">Clear filters</button>
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

	// Split any comma-separated "set" values (e.g. "7128, 7667") into individual tokens
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

	function renderFilters() {
		const container = document.getElementById('archive-filters');
		container.innerHTML = '';
		filterConfig.forEach(function(cfg) {
			const values = uniqueValues(cfg.key, cfg.multiToken);
			if (!values.length) return;

			const group = document.createElement('div');
			group.className = 'filter-group';

			const label = document.createElement('span');
			label.className = 'filter-group-label';
			label.textContent = cfg.label;
			group.appendChild(label);

			const pillWrap = document.createElement('div');
			pillWrap.className = 'filter-pills';

			values.forEach(function(val) {
				const pill = document.createElement('button');
				pill.type = 'button';
				pill.className = 'filter-pill';
				pill.dataset.category = cfg.key;
				pill.dataset.value = val;
				pill.textContent = val;
				if (selected[cfg.key].has(val)) pill.classList.add('active');
				pill.addEventListener('click', function() {
					if (selected[cfg.key].has(val)) {
						selected[cfg.key].delete(val);
					} else {
						selected[cfg.key].add(val);
					}
					renderFilters();
					renderGrid();
				});
				pillWrap.appendChild(pill);
			});

			group.appendChild(pillWrap);
			container.appendChild(group);
		});
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

	document.getElementById('clear-filters').addEventListener('click', function() {
		filterConfig.forEach(function(c) { selected[c.key].clear(); });
		renderFilters();
		renderGrid();
	});

	renderFilters();
	renderGrid();
</script>

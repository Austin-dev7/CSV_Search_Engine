// ===== CSV Search Engine (web version) =====
// Same graph logic as the Python version:
// build adjacency list from CSV -> direct parent mapping -> instant path lookup

let graph = {};        // node -> array of neighbors
let nodeSet = new Set();
let ready = false;

// ---- Load and parse the CSV ----
fetch('data/data.csv')
  .then(res => {
    if (!res.ok) throw new Error('Could not load data/data.csv');
    return res.text();
  })
  .then(text => {
    const lines = text.trim().split(/\r?\n/);
    // skip header row (Node,Neighbor)
    for (let i = 1; i < lines.length; i++) {
      const cols = lines[i].split(',');
      if (cols.length < 2) continue;
      const node = cols[0].trim();
      const neighbor = cols[1].trim();
      if (!node || !neighbor) continue;
      if (!graph[node]) graph[node] = [];
      graph[node].push(neighbor);
      nodeSet.add(node);
      nodeSet.add(neighbor);
    }
    ready = true;
    document.getElementById('status').textContent =
      `✅ Dataset loaded: ${nodeSet.size.toLocaleString()} nodes ready.`;
  })
  .catch(err => {
    document.getElementById('status').textContent = '❌ ' + err.message;
  });

// ---- BFS from start to target using direct parent mapping ----
function findPath(start, target) {
  if (!nodeSet.has(start)) return { error: `Invalid start node "${start}".` };
  if (!nodeSet.has(target)) return { error: `Invalid target node "${target}".` };
  if (start === target) return { path: [start], visited: 1 };

  const t0 = performance.now();

  const parent = { [start]: null };  // direct mapping: node -> its parent
  const queue = [start];
  let visited = 0;

  while (queue.length > 0) {
    const current = queue.shift();
    visited++;
    const neighbors = graph[current] || [];
    for (const next of neighbors) {
      if (!(next in parent)) {
        parent[next] = current;
        if (next === target) {
          // walk back through the parent map -> O(1) per step
          const path = [];
          let node = target;
          while (node !== null) {
            path.unshift(node);
            node = parent[node];
          }
          const t1 = performance.now();
          return { path, visited, time: ((t1 - t0) / 1000).toFixed(6) };
        }
        queue.push(next);
      }
    }
  }

  return { error: `No path found from ${start} to ${target}.` };
}

// ---- UI wiring ----
const btn = document.getElementById('searchBtn');
const resultBox = document.getElementById('result');
const errorBox = document.getElementById('error');

btn.addEventListener('click', () => {
  errorBox.classList.add('hidden');
  resultBox.classList.add('hidden');

  if (!ready) {
    errorBox.textContent = 'Dataset still loading — try again in a second.';
    errorBox.classList.remove('hidden');
    return;
  }

  const start = document.getElementById('start').value.trim();
  const target = document.getElementById('target').value.trim();

  if (!start || !target) {
    errorBox.textContent = 'Please enter both a start and a target node.';
    errorBox.classList.remove('hidden');
    return;
  }

  const res = findPath(start, target);

  if (res.error) {
    errorBox.textContent = res.error;
    errorBox.classList.remove('hidden');
    return;
  }

  document.getElementById('path').textContent = res.path.join(' -> ');
  document.getElementById('visited').textContent = res.visited.toLocaleString();
  document.getElementById('time').textContent = res.time;
  resultBox.classList.remove('hidden');
});

// Allow pressing Enter in the target field
document.getElementById('target').addEventListener('keydown', e => {
  if (e.key === 'Enter') btn.click();
});
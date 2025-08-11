function solution(edges) {
  const indegree = {};
  const outdegree = {};
  const nodes = new Set();

  // 간선 정보 저장
  for (const [u, v] of edges) {
    nodes.add(u);
    nodes.add(v);

    outdegree[u] = (outdegree[u] || 0) + 1;
    indegree[v] = (indegree[v] || 0) + 1;

    // 없는 키 초기화
    indegree[u] = indegree[u] || 0;
    outdegree[v] = outdegree[v] || 0;
  }

  let stickCount = 0;
  let eightCount = 0;
  let genNode = 0;

  // 모든 노드 순회
  for (const node of nodes) {
    const inDeg = indegree[node];
    const outDeg = outdegree[node];

    if (inDeg === 0 && outDeg >= 2) {
      genNode = node; // 생성 정점
    } else if (outDeg === 0 && inDeg >= 1) {
      stickCount++;
    } else if (inDeg >= 2 && outDeg >= 2) {
      eightCount++;
    }
  }

  const dounutCount = outdegree[genNode] - (stickCount + eightCount);

  return [genNode, dounutCount, stickCount, eightCount];
}

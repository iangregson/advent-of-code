const path = require('path')
const { promisify } = require('util')
const { readFile } = require('fs')
const read = promisify(readFile)

module.exports = { run }

function run() {
  return read(path.join(__dirname, 'input.txt'), 'utf-8')
    .then(data => data.trim().split('\n'))
    .then(makeGraph)
    .then(graph => ({
      part1: graph.searchAllEdges('0').size,
      part2: graph.countGroups().size
    }))
}

function makeGraph(groups) {
  class Graph {
    constructor(nodes = {}) {
      this.nodes = nodes
    }
    searchAllEdges(id, nodes = this.nodes, edges = new Set()) {
      edges.add(id)
      for (let nodeId of nodes[id].edges.filter(e => !edges.has(e))) {
        this.searchAllEdges(nodeId, nodes, edges)
      }
      return edges
    }
    countGroups() {
      return Object.keys(this.nodes)
        .map(id => this.searchAllEdges(id))
        .reduce((groups, edgeSet, i, allSets) => {
          groups.add(Array.from(edgeSet).sort().toString())
          return groups
        }, new Set())
    }
  }

  class Node {
    constructor(id, edges = []) {
      Object.assign(this, { id, edges })
    }
  }

  return Promise.resolve(groups)
    .then(groups => groups.map(g => g.split('<->'))
      .map(g => {
        let [id, edges] = g
        edges = edges.trim().split(', ')
        return new Node(id.trim(), edges)
      }).reduce((nodes, node) => {
        nodes[node.id] = node
        return nodes
      }, {}))
    .then(nodes => new Graph(nodes))
}



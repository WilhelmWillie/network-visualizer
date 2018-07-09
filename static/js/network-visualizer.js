var width = window.innerWidth,
    height = window.innerHeight;

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }))
    .force("charge", d3.forceManyBody().strength(-8))
    .force("center", d3.forceCenter(width / 2, height / 2));

d3.json("/network").then(function(network) {
  var link = svg.append("g")
      .attr("class", "links")
      .selectAll("line")
      .data(network.links)
      .enter().append("line")
      .attr("stroke-width", function(d) { return d.value });

  var node = svg.append("g")
      .attr("class", "nodes")
      .selectAll("circle")
      .data(network.nodes)
      .enter().append("circle")
      .attr("r", function(d) {
        var id = d.id;

        if (id === 'origin') {
          return 30;
        } else if (id.startsWith("company ")) {
          return 5;
        } else {
          return 5;
        }
      })
      .attr("fill", function(d) {
        var id = d.id;

        if (id.startsWith("company ")) {
          return "#254278";
        }

        if (id.startsWith("connection ")) {
          return "#257830";
        }

        return "#636363";
      });

  simulation.nodes(network.nodes).on("tick", ticked);
  simulation.force("link").links(network.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  }
});
var pyDateFormatter = function(pythonDate) {
    return pythonDate.substring(0, pythonDate.length - 5);
}
var THERMISTOR = 1;

// http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/dynamic-update/
$(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });

        // @NOTE: May need to do timezone offset
        // 
        // https://stackoverflow.com/questions/9229213/convert-iso-date-to-milliseconds-in-javascript
        /*
           JSON data coming back:
            {
                "thermistor": "http://localhost:8000/api/v1/thermistors/1/", 
                "temp": "21", 
                "created_on": "2014-07-26T13:53:38.067Z", 
                "url": "http://localhost:8000/api/v1/temperatures/2/"
            }
        */
        $.getJSON("http://localhost:8000/api/v1/temperatures/", {thermistor__index: THERMISTOR}, function(data) {
          var graph_data = [];
          $.each(data.results, function(i, obj) {
            //console.log(obj.thermistor + ': ' + obj.temp);
            // NOTE: multiplying x by 1000 used to initialize the graph size properly
            graph_data.push({x: (new Date(obj.created_on)).getTime(), y: Number(obj.temp)});
          });
          //console.log(graph_data);
          createGraph(graph_data);
        });

        var pydateToNumber = function(pythonDate) {
        };
    
        var createGraph = function(data) {
            var chart;
            $('#graph').highcharts({
                chart: {
                    type: 'spline',
                    animation: Highcharts.svg, // don't animate in old IE
                    marginRight: 10,
                    events: {
                        load: function() {
                            // set up the updating of the chart each second
                            var series = this.series[0];
                            setInterval(function() {
                                $.getJSON("http://localhost:8000/api/v1/temperatures/", {thermistor__index: THERMISTOR}, function(data) {
                                    data = data.results;
                                    var x = (new Date(data[0].created_on)).getTime(),
                                        y = Number(data[0].temp);
                                    //console.log('new data: ' + x + ', ' + y);
                                    series.addPoint([x, y], true, true);
                                });
                            }, 1000);
                        }
                    }
                },
                title: {
                    text: 'Live temperature feed'
                },
                credits: {
                    text: '',
                },
                xAxis: {
                    type: 'datetime',
                    tickPixelInterval: 150,
                    title: {
                        text: 'Time'
                    }
                },
                yAxis: {
                    title: {
                        text: 'Temperature - C'
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#808080'
                    }]
                },
                tooltip: {
                    formatter: function() {
                            return '<b>'+ this.series.name +'</b><br/>'+
                            Highcharts.dateFormat('%H:%M:%S', this.x) +'<br/>'+
                            Highcharts.numberFormat(this.y, 2);
                    }
                },
                legend: {
                    enabled: false
                },
                exporting: {
                    enabled: false
                },
                series: [{
                    name: 'Temperature',
                    data: (function() {

                        var empty_data = [];
                        var    time = (new Date()).getTime(),
                            i;
        
                        for (i = -19; i <= 0; i++) {
                            empty_data.push({
                                x: time + i * 1000,
                                y: 0
                            });
                        }
                        return empty_data;
                    })()
                }]
            });
        };
});

$(function(){
    /*
    * @require AgentAPI
    */
    "use strict"
    var map = L.map('map').setView([-30.09316, 84.21604], 12)
    L.tileLayer('http://10.67.4.121/osm/1.0.0/brasil/{z}/{x}/{y}.png',{
        minZoom : 1,
        crs : L.CRS.EPSG4326,
        tms : true,
        continuousWorld : true,
        noWrap : true
    }).addTo(map)

    var popup = L.popup();

    var sideBar = L.control.sidebar('sidebar',{
        position : 'right',
        closeButton : false,
        autoPan : false
    });

    map.addControl(sideBar);

    setTimeout(function(){sideBar.show()},500);

    function updateModel(){

    }

    function renderTable(){

    }

    function updateAgentsModel(){
        var promise = AgentAPI.getAllAgents();
        promise.done(function(){

        })

        promise.fail(function(){

        })
    }
})


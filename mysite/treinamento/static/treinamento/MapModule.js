/*
* @require AgentAPI
* @require L from leaflet
*/

var MapModule = (function(){
    var agents = []
    var markers = new L.FeatureGroup();
    var map = undefined;
    var sidebar = undefined;
    var agentIcon = undefined;

    function _initMap(){
        map = L.map('map').setView([-30.09316, 84.21604], 12);
        //MapServer
        L.tileLayer('http://10.67.4.121/osm/1.0.0/brasil/{z}/{x}/{y}.png',{
            minZoom : 1,
            crs : L.CRS.EPSG4326,
            tms : true,
            continuousWorld : true,
            noWrap : true
        }).addTo(map);

        //SideBar
        sideBar = L.control.sidebar('sidebar',{
            position : 'right',
            closeButton : false,
            autoPan : false
        });
        setTimeout(function(){sideBar.show()},500);
        sideBar.addTo(map);
        //Marker
        agentIcon = L.icon({
            iconUrl : 'static/treinamento/img/agent.png',
            iconSize : [50,50],
            // popupAnchor : [-3, -76]
        });
    }

    function _loop(){
        var promise = AgentAPI.getAllAgents();
        promise.done(function(data){
            agents = data;
            _render();
        });

        promise.fail(function(){
            console.log("The server found a problem when retrieving agents");
        });

        promise.always(function(){
            setTimeout(_loop,100);
        });
    }

    function _render(){
        _renderTable();
        _renderAgents();
    }

    function _renderTable(){

    }

    function _renderAgents(){
        //Remove old markers
        map.removeLayer(markers)
        //Add new markers
        var arrayLength = agents.length;
        markers = new L.FeatureGroup();
        for(var i = 0; i < arrayLength; i++){
            var agent = agents[i];
            if(_isAgentGeoLocated(agent)){
                var marker = L.marker([agent.lat,agent.lon],{icon : agentIcon});
                markers.addLayer(marker);
            }
        }
        map.addLayer(markers);
    }

    function _isAgentGeoLocated(agent){
        if(agent.lat == undefined || agent.lon == undefined){
            return false;
        }
        else if(agent.lat <= 90 && agent.lat >= -90 && agent.lon <= 180 && agent.lon >= -180){
            return true;
        }
    }

    return{
        init : function(){
            $(function(){
                _initMap();
                _loop();
            })
        }
    }
}());

MapModule.init();